##############################################################
#
# copyLocalServer v1.2
# Author: Jammy Chong
# Copyright (c) 2021 Rellum LLC
# Email: rellumcreative@gmail.com
# Last Update: 07-30-2021
##############################################################
"""
Copies files or folders according to the selected option
from the Windows Explorer right-click menu options.
The selected option is recieve as an action argument which follows:
  action 0: copy to local
  action 1: copy to server
  action 2: overwrite to local
  action 3: overwrite to server
"""

import sys
import os
import shutil
import time
import subprocess

action = int(sys.argv[1])
_file = sys.argv[2]
directory = os.path.dirname(_file)


def write_temp_txt(_file, suffix, message):
    """
    Creates a text file with the name of the file and
    a suffix at the end to display message.
    Contents of the text files have a more detail message.
    """
    temp_file, temp_ext = os.path.splitext(_file)
    temp_file += "{}.txt".format(suffix)
    with open(temp_file, 'w') as f:
        f.write("{0} {1}".format(temp_file, message))
    return temp_file


def copy_to_drive(action, _file, new_directory, new_file):
    """
    Copies the given file into the corresponding directory,
    creates text files in the current directory to display messages.
    """
    if not os.path.exists(new_directory):
        try:
            os.makedirs(new_directory, exist_ok=True)
        except:
            pass

    if action in (0, 1):
        if os.path.exists(new_file):
            write_temp_txt(_file, "_exists", 
                           "already exists, use copy/overwrite instead")
            return
    try:
        copy_txt = write_temp_txt(_file, "_copying", "Copying file")
        time.sleep(0.5)
        if os.path.isdir(_file):
            if not os.path.exists(new_file):
                shutil.copytree(_file, new_file)
            else:
                subprocess.call(["xcopy", _file, new_file, 
                                "/v", "/e", "/y"])
        else:
            shutil.copy(_file, new_file)
        os.remove(copy_txt)
        if action in (2, 3):
            temp_file, temp_ext = os.path.splitext(_file)
            for suffix in ("_exists.txt", "_check_folder.txt"):
                temp_suffix = temp_file + "_exists.txt"
                if os.path.exists(temp_suffix):
                    try:
                        os.remove(temp_suffix)
                    except:
                        pass
    except:
        pass


def copy_main(action, local, server):
    """
    Copies the file according to the copying type selected by the user
    """
    if action in (0, 2):
        drive1 = local
        drive2 = server
    else:
        drive1 = server
        drive2 = local

    if _file.lower().startswith(drive2.lower()):
        drive_directory = drive1 + directory[len(drive2):]
        drive_file = drive1 + _file[len(drive2):]
        if action in (0, 2) or os.path.exists(os.path.splitdrive(drive_directory)[0]):
            copy_to_drive(action, _file, drive_directory, drive_file)
        else:
            write_temp_txt(_file, "_not_connected", "Not connected to server network")
    else:
        try:
            write_temp_txt(_file, "_check_folder", "Not in local/server folder")
        except:
            pass


def main(action):
    settings = os.path.dirname(sys.argv[0]).replace("scripts", "\\settings.txt")
    with open(settings, 'r') as d:
        data = d.readlines()
    local = data[1].split("=")[1]
    local = local.replace("\n", "")
    server = data[2].split("=")[1]
    server = server.replace("\n", "")
    copy_main(action, local, server)


main(action)