# Common parts, including commands over SMP

# GSE Proprietary Software License
# Copyright (c) 2025 Global Satellite Engineering, LLC. All rights reserved.
# This software and associated documentation files (the "Software") are the proprietary and confidential information of Global Satellite Engineering, LLC ("GSE"). The Software is provided solely for the purpose of operating applications distributed by GSE and is subject to the following conditions:

# 1. NO RIGHTS GRANTED: This license does not grant any rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell the Software.
# 2. RESTRICTED ACCESS: You may only access the Software as part of a GSE application package and only to the extent necessary for operation of that application package.
# 3. PROHIBITION ON REVERSE ENGINEERING: You may not reverse engineer, decompile, disassemble, or attempt to derive the source code of the Software.
# 4. PROPRIETARY NOTICES: You must retain all copyright, patent, trademark, and attribution notices present in the Software.
# 5. NO WARRANTIES: The Software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.
# 6. LIMITATION OF LIABILITY: In no event shall GSE be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Software or the use or other dealings in the Software.
# 7. TERMINATION: This license will terminate automatically if you fail to comply with any of the terms and conditions of this license. Upon termination, you must destroy all copies of the Software in your possession.

# THE SOFTWARE IS PROTECTED BY UNITED STATES COPYRIGHT LAW AND INTERNATIONAL TREATY. UNAUTHORIZED REPRODUCTION OR DISTRIBUTION IS SUBJECT TO CIVIL AND CRIMINAL PENALTIES.

from . import smp
from .smp_exceptions import *
from gse_gsatmicro_utils import utils
from gse_gsatmicro_utils import detect_ports
import sys
from tqdm import tqdm
import math
import cbor2
from python_minifier import minify
import json
import posixpath as pp
import base64
import importlib

#######################################################################################################################
# Local functions and data

# MTU used by MCUboot, must be known in advance because it can't be interrogated
MCUBOOT_MTU = 2048
# Default timeout for the "run python" SMP command
DEFAULT_RUNPY_TO_S = 5

# Code for clean_run_prog() function below
clean_run_prog_code = """
import utils
import {mod_name}

try:
    {mod_name} = utils.reload({mod_name})
    utils.run({mod_name}.{func_name})
    eprint("true")
except:
    eprint("false")
"""

#######################################################################################################################
# Public interface

# A simple configuration object that is shared between various modules
class Config:
    def __init__(self, ser=None, args=None):
        self.ser = ser
        self.args = args

    @property
    def timeout(self):
        return getattr(self.args, "timeout", DEFAULT_RUNPY_TO_S)

# Single configuration instance accessible from other modules.
# Must be initialised by calling init() below.
cfg = Config()

# Class used to handle progress bars
class ProgressBar:

    # Progress bar kinds: none (not displayed), log (log messages), full (tqdm)
    (NONE, LOG, FULL) = range(3)

    def __init__(self, kind=None):
        if kind == None: # detect automatically
            kind = self.FULL if sys.stdout.isatty() and utils.get_debug_level() <= 1 else self.LOG
        self.kind, self.pb = kind, None

    # Create the progress bar with the given "total" units
    def start(self, total):
        if self.kind == self.NONE or total == 0: # don't show any progress report for 0-sized requests
            return
        if self.kind == self.LOG:
            self.pb = (0, total)
        else: # use full progress bar
            if total >= 10000: # switch to kb for anything that's at least 100000 bytes in size
                self.pb = tqdm(total = total, unit='KB', unit_scale=True, unit_divisor=1024)
            else:
                self.pb = tqdm(total = total)

    # Update progress
    def update(self, amount):
        if self.pb is None:
            return
        if self.kind == self.LOG:
            (crt, total) = self.pb
            crt += amount
            utils.debug2("Progress: {}/{} bytes".format(crt, total))
            self.pb = (crt, total)
        elif self.kind == self.FULL:
            self.pb.update(amount)

    # Close progress bar
    def close(self):
        if self.pb is None:
            return
        if self.kind == self.FULL:
            self.pb.close()

    # Generic callback progress function
    def cb(self, act, data=None):
        if act == "start":
            self.start(data)
        elif act == "update":
            self.update(data)
        else:
            self.close()

# Initialise the serial port and user arguments
def init(ser, args, config):
    cfg.ser = ser
    cfg.args = args
    cfg.cfg = config

# Return the maximum available space for data, given an MTU and the remote info without any actual data
def get_available_space_for_data(mtu, info, data_field_name):
    # Start with a very optimistic estimation:
    #    - the UART header takes 4 bytes
    #    - the rest contains an encoded frame, a length field (2 bytes), a CRC (another 2 bytes) and the encoded data,
    #      all encoded in Base64
    v = mtu - 4 - math.ceil((smp.Frame.ENCODED_LEN + 4 + len(cbor2.dumps(info))) * 4 / 3)
    # Take into account the Base64 encoding
    v = math.ceil(v * 3 / 4)
    # Use a file upload request in the frame, this isn't important as we're only interested in the len
    frame = smp.Frame(smp.OPCODE_WRITE, smp.AppGroup.ID, smp.AppGroup.CMD_IMG_UPLOAD)
    # Now decrease this until everything fits in a frame of the given MTU
    while v > 0:
        info[data_field_name] = b'0' * v
        res = smp.encode_request(frame, info, mtu, 0, skip_if_overflow=True)
        if res != False:
            assert len(res) == 1
            break
        v -= 1
    assert v > 0
    return v

# Returns the SMP MTU used on the device or None if the MTU can't be read from the device
def get_upload_mtu(ser):
    v, in_recovery, bad_response = None, False, False
    try:
        resp_data = smp.send_request(ser, smp.OPCODE_READ, smp.GSEGroup.ID, smp.GSEGroup.CMD_GET_LIMITS, {})
        v = resp_data.get("mtu", None)
    except InvalidResponseData as e:
        if e.num_rc== smp.MCUMGR_ERR_ENOTSUP:
            in_recovery, v = True, MCUBOOT_MTU
        else:
            bad_response = True
    except Exception as e:
        bad_response, err = True, e
    if bad_response:
        utils.debug("Device didn't respond correctly to 'get limits' command, this shouldn't happen")
        utils.debug("Exception was {} with text {}".format(type(err).__name__, str(err)))
        v = None
    if v == None or not isinstance(v, int):
        utils.warning("Invalid response to 'get limits', data either missing or of invalid type")
        v = None
    # Use default MTU if actual MTU can't be determined
    if v == None:
        v = smp.DEFAULT_MTU
    if in_recovery:
        utils.info("Detected MCUboot recoery mode")
    utils.info("Upload MTU is {} bytes".format(v))
    return v, in_recovery

# Download the given file from the device, writing the output to the stream "f"
# If "cleanup" is True, also execute the "file close" operation on target
def download_file(fname, f, cleanup=False, progress_cb=lambda act, data=None: None):
    ser = cfg.ser
    with ser.keep():
        crt, tot_len, seq_no = 0, None, smp.get_next_seq_no(None)
        while tot_len == None or crt < tot_len:
            to = smp.get_command_timeout(smp.FileGroup.ID, smp.FileGroup.CMD_FILE_DL_UP) if tot_len == None else smp.SMP_DEFAULT_RX_TIMEOUT_S
            resp_data = smp.send_request(ser, smp.OPCODE_READ, smp.FileGroup.ID, smp.FileGroup.CMD_FILE_DL_UP, {"off": crt, "name": fname},
                seq_no=seq_no, timeout=to, skip_rc_check=True)
            if "rc" in resp_data:
                rc, _ = smp.decode_error_in_response(resp_data)
                if rc == smp.MCUMGR_ERR_ENOENT:
                    utils.error("File not found on target")
                    raise FileNotFoundError(f"{fname} not found on target")
                raise InvalidResponseData("Unexpected response to 'file download'", resp_data)
            if resp_data.get("off", None) != crt:
                raise InvalidResponseData("Bad offset in file download response", {})
            crt_len = len(resp_data["data"])
            if crt == 0: # the first response contains the total length
                tot_len = resp_data["len"]
                utils.info("Download file {} (size is {})".format(fname, tot_len))
                progress_cb("start", tot_len)
            f.write(resp_data["data"])
            crt += crt_len
            progress_cb("update", crt_len)
            seq_no = smp.get_next_seq_no(seq_no)
        progress_cb("close")
        if cleanup:
            smp.send_request(ser, smp.OPCODE_WRITE, smp.FileGroup.ID, smp.FileGroup.CMD_FILE_CLOSE, {}, skip_rc_check=True)

# Upload the given data to the device at the given destination
# If "cleanup" is True, also execute the "file close" operation on target
def upload_file(fname, data, cleanup=False, progress_cb=lambda act, data=None: None):
    ser = cfg.ser
    with ser.keep():
        # Figure out how much data we can send in a single package, based on the MTU.
        # Since the first and next packages are different, we need different values to maximize speed
        upload_mtu, in_recovery = get_upload_mtu(ser)
        assert not in_recovery
        img_info = {"off": 0, "data": b'', "name": fname, "len": len(data)}
        first_available = get_available_space_for_data(upload_mtu, img_info, "data")
        utils.debug2("Available size for data in first request: {}".format(first_available))
        # And now for the next package
        img_info = img_info = {"off": len(data), "data": b'', "name": fname}
        next_available = get_available_space_for_data(upload_mtu, img_info, "data")
        utils.debug2("Available size for data in the next requests: {}".format(next_available))
        off, seq_no = 0, smp.get_next_seq_no(None)
        progress_cb("start", len(data))
        while len(data) == 0 or off < len(data): # allow uploading files of size 0
            if off == 0:
                file_info = {"off": 0, "data": data[:first_available], "name": fname, "len": len(data)}
            else:
                file_info = {"off": off, "data": data[off:off + next_available], "name": fname}
            # Send current request
            to = smp.get_command_timeout(smp.FileGroup.ID, smp.FileGroup.CMD_FILE_DL_UP) if off == 0 else smp.SMP_DEFAULT_RX_TIMEOUT_S
            resp_data = smp.send_request(ser, smp.OPCODE_WRITE, smp.FileGroup.ID, smp.FileGroup.CMD_FILE_DL_UP, file_info, upload_mtu, seq_no, timeout=to)
            if not 'off' in resp_data:
                raise InvalidResponseData("Unexpected response to 'image upload'", resp_data)
            # Read back offset from MCU and use it as the new offset value
            mcu_off = resp_data["off"]
            progress_cb("update", mcu_off - off)
            off = mcu_off
            seq_no = smp.get_next_seq_no(seq_no)
            if len(data) == 0: # we need to make a single request for an empty file
                break
        progress_cb("close")
        if cleanup:
            smp.send_request(ser, smp.OPCODE_WRITE, smp.FileGroup.ID, smp.FileGroup.CMD_FILE_CLOSE, {}, skip_rc_check=True)

# Reset the device
def do_reset(ser):
    smp.send_request(ser, smp.OPCODE_WRITE, smp.DefaultGroup.ID, smp.DefaultGroup.CMD_RESET, None)

# Generic run program: run the given program with the given arguments, make sure that its output as valid JSON and return
# the parsed JSON
def run_prog(prog, *args, **kwargs):
    code = prog.format(*args, **kwargs)
    code = minify(code, rename_locals=True, rename_globals=True, constant_folding=True, combine_imports=True)
    req_data = {"code": code, "to": cfg.timeout}
    resp = smp.send_request(cfg.ser, smp.OPCODE_READ, smp.GSEGroup.ID, smp.GSEGroup.CMD_RUN_PYTHON, req_data)
    return str(resp["out"], "ascii") if isinstance(resp['out'], bytes) else resp['out']

# Same as "run_prog", but check that the program's response is valid JSON
# Returns the parsed JSON object
def run_prog_json(prog, *args, **kwargs):
    return json.loads(run_prog(prog, *args, **kwargs))

# Return the maximum available space for an EXTRO upload, given an MTU and the remote info without any actual data
def get_available_space_for_extro_upload(mtu, info, data_field_name):
    # Use an EXTRO upload request in the frame
    frame = smp.Frame(smp.OPCODE_WRITE, smp.GSEGroup.ID, smp.GSEGroup.CMD_EXTRO_DATA)
    # Divide and conquer our way to the optimal data size
    low, high, prev_v, v_ok = 0, mtu, None, 0
    while True:
        if (v := (low + high) // 2) == prev_v: # found our value
            break
        info[data_field_name] = b'\xFF' * v
        res = smp.encode_request(frame, info, mtu, 0, skip_if_overflow=True)
        if res == False: # this doesn't encode in a single frame
            high = v
        else:
            assert len(res) == 1
            low, v_ok = v, max(v_ok, v)
        prev_v = v
    assert v_ok > 0
    return v_ok

# Upload the given ROMFS image to the device
# Returns mount_status as sent by the device (if applicable)
def upload_romfs(data, progress_cb=lambda act, data=None: None):
    ser = cfg.ser
    with ser.keep():
        # Figure out how much data we can send in a single package, based on the MTU.
        upload_mtu, in_recovery = get_upload_mtu(ser)
        assert not in_recovery
        extro_info = {"off": 0, "data": b''}
        data_available = get_available_space_for_extro_upload(upload_mtu, extro_info, "data")
        utils.debug2("Available size for data in EXTRO upload request: {}".format(data_available))
        # Start an EXTRO upload
        smp.send_request(ser, smp.OPCODE_WRITE, smp.GSEGroup.ID, smp.GSEGroup.CMD_EXTRO_START, {"size": len(data)})
        # Then send the data
        off, seq_no, to = 0, smp.get_next_seq_no(None), smp.get_command_timeout(smp.GSEGroup.ID, smp.GSEGroup.CMD_EXTRO_DATA)
        progress_cb("start", len(data))
        while len(data) == 0 or off < len(data): # allow uploading files of size 0 (remove ROMFS)
            crt = min(len(data) - off, data_available)
            extro_info = {"off": off, "data": data[off:off + crt]}
            # Send current request
            resp_data = smp.send_request(ser, smp.OPCODE_WRITE, smp.GSEGroup.ID, smp.GSEGroup.CMD_EXTRO_DATA, extro_info, upload_mtu,
                                        seq_no, timeout=to)
            progress_cb("update", crt)
            off += crt
            seq_no = smp.get_next_seq_no(seq_no)
            if len(data) == 0:
                break
        progress_cb("close")
        # The last response data must have the "m" field that contain the result of the mounting operation
        m_flag = None
        if data and (m_flag := resp_data.get("m", None)) == None:
            utils.warning("Can't find mount status indication in final EXTRO upload package")
        return m_flag

# Run the function in the given module, making sure to reimport it first
# Returns True for success or False for error
def run_code_clean(mod_name, func_name):
    return run_prog_json(clean_run_prog_code, mod_name=mod_name, func_name=func_name)

# Return the package version or None for error
def get_version():
    try:
        return importlib.metadata.version(__name__.split(".")[0])
    except:
        return "UNKNOWN"


# Return all the ports detected for the device with the given serial numner.
# Use None to skip serial number matching and return all the detected ports for all connected devices.
def get_detected_ports(cmdline_sernum):
    try:
        detected = detect_ports.detect()
    except:
        detected = {}
    # Optional serial number filtering
    detected = {k: v for k, v in detected.items() if (cmdline_sernum == None) or (k == cmdline_sernum)}
    return detected

#######################################################################################################################
# Implementation of commands used in various servers (currently httpd and cond)

# API version
api_version = "2.0"

# Request-specific exception classes
class RequestError(Exception):
    pass

class InvalidRequest(RequestError):
    pass

class PathNotFound(RequestError):
    def __init__(self, path):
        super().__init__(f"path {path} not found")
        self.path = path

# Validate the JSON request
# 'mandatory' is a list with the mandatory keys in the request dictionary
# 'optional' is a list with the optional keys in the request dictionary
def check_req(request, mandatory, optional=None):
    # Either way, we expect a dictionary with all our POST data
    if not isinstance(request, dict):
        raise InvalidRequest("the request is not a dictionary")
    # Check keys
    d_set = set(list(request.keys())) # request keys
    m_set = set(mandatory) # mandatory keys
    a_set = m_set | set(optional or []) # all keys (mandatory and optional)
    if d_set - a_set: # foreign keys found
        raise InvalidRequest("foreign keys found in the request")
    if m_set - d_set: # not all mandatory keys were specified
        raise InvalidRequest("mandatory fields not found in the request")
    return request

# List the content of the directory at "path". If "stat" is True, it also returns data about each item in the directory
# (see fs_stat below for mode details). If not specified, "stat" defaults to False.
# Returns a dictionary where the keys are directory items and the values are stat data (emtpy if "stat" is False)
def fs_list(fs, req, logger):
    with cfg.ser.keep():
        check_req(req, ("path", ), ("stat", ))
        if not (do_stat := req.get("stat", False)) in (True, False):
            raise InvalidRequest("invalid stat")
        path, res = req["path"], {}
        if fs.fs_find(path, must_exist=False) != "dir": # the requested path must exist
            raise PathNotFound(path)
        logger.debug(f"LIST {req['path']}")
        for i in fs.listdir(path):
            t, item_path = {}, pp.join(path, i)
            if do_stat:
                if (s := fs.stat(item_path)) == False: # might happen in case the device changes the FS
                    raise PathNotFound(item_path)
                t = {"kind": "dir" if fs.is_stat_dir(s[0]) else "file", "size": s[6], "readonly": fs.is_stat_ro(s[0])}
            res[i] = t
        return res

# Return information about a file system item (file or directory).
# Returns a {"kind": "file" | "dir", "size": size, "readonly": True|False} dictionary
def fs_stat(fs, req, logger):
    with cfg.ser.keep():
        check_req(req, ("path", ))
        path = req["path"]
        logger.debug(f"STAT {path}")
        if fs.fs_find(path, must_exist=False) == "none": # the item must exist
            raise PathNotFound(path)
        res = fs.stat(path)
        return {"kind": "dir" if fs.is_stat_dir(res[0]) else "file", "size": res[6], "readonly": fs.is_stat_ro(res[0])}

# Returns the kind of item ("file, "dir" or "none") that the given path points to.
# "none" means that the item does not exist
def fs_kind(fs, req, logger):
    check_req(req, ("path", ))
    logger.debug(f"FIND {req['path']}")
    return fs.fs_find(req["path"], must_exist=False)

# Return the content of file at "path"
def fs_get(fs, req, logger):
    with cfg.ser.keep():
        check_req(req, ("path", ))
        path = req["path"]
        logger.debug(f"GET {path}")
        if fs.fs_find(path, must_exist=False) != "file":
            raise PathNotFound(path)
        # Read file content and return it
        # The files are expected to be small, so no streaming is needed.
        f = fs.open(path, "rb")
        res = f.read()
        f.close()
        return res

# Create a file or a directory at "path", depending on "kind" (which must be either "file" or "dir")
# TODO: add "overwrite"
def fs_create(fs, req, logger):
    with cfg.ser.keep():
        check_req(req, ("path", "kind"))
        if not req["kind"] in ("file", "dir"):
            raise InvalidRequest("invalid kind")
        path = req["path"]
        logger.debug(f"CREATE {path} kind={req['kind']}")
        if req["kind"] == "dir":
            fs.mkdir(path)
        else:
            fs.mkfile(path)

# Remove a file or a directory from "path", depending on "kind" (which must be either "file" or "dir")
def fs_remove(fs, req, logger):
    with cfg.ser.keep():
        check_req(req, ("path", "kind"))
        if not req["kind"] in ("file", "dir"):
            raise InvalidRequest("invalid kind")
        path = req["path"]
        logger.debug(f"REMOVE {path} kind={req['kind']}")
        if (kind := fs.fs_find(path, must_exist=False)) == "none": # item must exist
            raise PathNotFound(path)
        if kind != req["kind"]: # item kind (file/dir) must match requested "kind"
            raise InvalidRequest("mismatched kind")
        if req["kind"] == "dir":
            fs.rmdir(path)
        else:
            fs.remove(path)

# Save data from "file" at "path", which must not xist.
# Optionally, "overwrite" can be specified to overwrite existing files (defaults to True if not specified).
def fs_put(fs, req, logger, b64=False):
    with cfg.ser.keep():
        check_req(req, ("path", "file"), ("overwrite", ))
        path, fdata, overwrite = req["path"], req["file"], req.get("overwrite", True)
        if b64:
            fdata = base64.b64decode(fdata)
        logger.debug(f"PUT path={path} overwrite={overwrite}")
        with fs.locked():
            # Does this path exist?
            kind = fs.fs_find(path, must_exist=False)
            if kind == "dir": # path is a directory, return with error
                raise InvalidRequest("path is a directory")
            elif kind == "file" and not overwrite: # proceed only if allowed to overwrite path
                raise InvalidRequest("file already exists")
            # Write data to file
            if isinstance(fdata, str):
                fdata = fdata.encode(errors='replace')
            f = fs.open(path, "wb")
            f.write(fdata)
            f.close()

# Return the API and gsemgr version
def cmd_version(fs, req, logger):
    logger.debug("version request")
    return {"api": api_version, "gsemgr": get_version()}

# Reset the board
# TODO: this could be smarter. For example: automatically wait for the needed ports to become available again
def cmd_reset(fs, req, logger):
    logger.debug("RESET")
    do_reset(cfg.ser)

# Run the code given in "func". The syntax must be "mod_name.func_name"
# Return the function output or False for error
def cmd_run_code(fs, req, logger):
    check_req(req, ("func", ))
    parts = req["func"].split(".") # ensure mod_name.func_name syntax
    if len(parts) != 2:
        raise InvalidRequest("invalid function name")
    logger.debug(f"RUN {req['func']}")
    try:
        res = run_code_clean(parts[0], parts[1])
    except:
        res = False
    return res