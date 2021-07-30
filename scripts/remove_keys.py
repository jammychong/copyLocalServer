##############################################################
#
# copyLocalServer v1.2
# Author: Jammy Chong
# Copyright (c) 2021 Rellum LLC
# Email: rellumcreative@gmail.com
# Last Update: 07-30-2021
##############################################################
"""
Removes Keys created in the registry.
"""

from winreg import *

keys = ["CopyLocal", "CopyServer", 
        "CopyOverwriteLocal", "CopyOverwriteServer"]

for base in ("*", "Folder"):
    for key in keys:
        try:
            key_path = "{}\\shell\\{}".format(base, key)
            open_key = OpenKey(HKEY_CLASSES_ROOT, key_path, 
                            0, KEY_ALL_ACCESS)
            subkey = EnumKey(open_key, 0)
            DeleteKey(open_key, subkey)
            DeleteKey(HKEY_CLASSES_ROOT, key_path)
        except:
            pass