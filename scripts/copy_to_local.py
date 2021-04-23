import sys
import os
import shutil

_file = sys.argv[1]
directory = os.path.dirname(_file)


def write_temp_txt(_file, suffix, message):
    temp_file, temp_ext = os.path.splitext(_file)
    temp_file += "{}.txt".format(suffix)
    with open(temp_file, 'w') as f:
        f.write("{0} {1}".format(temp_file, message))
    

def copy_to_local(_file, local_directory, local_file):
    if not os.path.exists(local_directory):
        try:
            os.makedirs(local_directory, exist_ok=True)
        except:
            pass

    if os.path.exists(local_file):
        write_temp_txt(_file, "_exists", "already exists, use copy/overwrite instead")
    else:
        try:
            shutil.copy(_file, local_file)
        except:
            pass

settings = os.path.dirname(sys.argv[0]).replace("scripts", "\\settings.txt")
with open(settings, 'r') as d:
    data = d.readlines()

local = data[1].split("=")[1]
local = local.replace("\n", "")
server = data[2].split("=")[1]
server = server.replace("\n", "")

if _file.lower().startswith(server.lower()):
    local_directory = local + directory[len(server):]
    local_file = local + _file[len(server):]
    copy_to_local(_file, local_directory, local_file)
else:
    try:
        write_temp_txt(_file, "_check_folder", "Not in local/server folder")
    except:
        pass