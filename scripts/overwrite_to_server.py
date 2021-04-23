import sys
import os
import shutil
import time

_file = sys.argv[1]
directory = os.path.dirname(_file)


def write_temp_txt(_file, suffix, message):
    temp_file, temp_ext = os.path.splitext(_file)
    temp_file += "{}.txt".format(suffix)
    with open(temp_file, 'w') as f:
        f.write("{} {}".format(temp_file, message))
    return temp_file


def copy_to_server(_file, server_directory, server_file):
    if not os.path.exists(server_directory):
        try:
            os.makedirs(server_directory, exist_ok=True)
        except:
            pass

    try:
        copy_txt = write_temp_txt(_file, "_copying", "Copying file")
        time.sleep(0.5)
        shutil.copy(_file, server_file)
        os.remove(copy_txt)
        temp_file, temp_ext = os.path.splitext(_file)
        for suffix in ("_exists.txt", "_check_folder.txt", "_not_connected.txt"):
            temp_suffix = temp_file + "_exists.txt"
            if os.path.exists(temp_suffix):
                try:
                    os.remove(temp_suffix)
                except:
                    pass
    except:
        pass

settings = os.path.dirname(sys.argv[0]).replace("scripts", "\\settings.txt")
with open(settings, 'r') as d:
    data = d.readlines()

local = data[1].split("=")[1]
local = local.replace("\n", "")
server = data[2].split("=")[1]
server = server.replace("\n", "")

if _file.lower().startswith(local.lower()):
    server_directory = server + directory[len(local):]
    server_file = server + _file[len(local):]
    if os.path.exists(os.path.splitdrive(server_directory)[0]):
        copy_to_server(_file, server_directory, server_file)
    else:
        write_temp_txt(_file, "_not_connected", "Not connected to server network")
else:
    try:
        write_temp_txt(_file, "_check_folder", "Not in local/server folder")
    except:
        pass