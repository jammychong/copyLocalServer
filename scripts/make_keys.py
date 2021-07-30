##############################################################
#
# copyLocalServer v1.2
# Author: Jammy Chong
# Copyright (c) 2021 Rellum LLC
# Email: rellumcreative@gmail.com
# Last Update: 07-30-2021
##############################################################
"""
Generate keys in the register, copyToDrive options available
by right-clicking file or folder in Windows Explorer.
Copy Options run a python script with the given action:
  action 0: copy to local
  action 1: copy to server
  action 2: overwrite to local
  action 3: overwrite to server
"""

import os
import sys
import winreg as reg

# Get path of current working directory and python.exe
cwd = os.getcwd()
python_exe = sys.executable

hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"
parse_var = f'"%1"'


def make_key_values(base):
    key_values = [(r'{}\\shell\\CopyLocal\\'.format(base), 
                  '&Copy to local', 'copy_file.py'),
                  (r'{}\\shell\\CopyServer\\'.format(base), 
                  '&Copy to server', 'copy_file.py'),
                  (r'{}\\shell\\CopyOverwriteLocal\\'.format(base), 
                  '&Copy/Overwrite to local', 'copy_file.py'),
                  (r'{}\\shell\\CopyOverwriteServer\\'.format(base), 
                  '&Copy/Overwrite to server', 'copy_file.py')]
    return key_values


key_values_file = make_key_values("*")
key_values_directory = make_key_values("Folder")

for key_values in (key_values_file, key_values_directory):
    for i in range(len(key_values)):
        key_path = key_values[i][0]
        key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
        reg.SetValue(key, '', reg.REG_SZ, key_values[i][1])
        reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, f'{cwd}\\icon.ico')
        key_cmd = reg.CreateKey(key, r"command")
        reg.SetValue(key_cmd, '', reg.REG_SZ, python_exe + 
                f' "{cwd}\\scripts\\{key_values[i][2]}" "{i}" {parse_var}')
        reg.SetValue(key_cmd, '', reg.REG_SZ, hidden_terminal + 
                f' "{cwd}\\scripts\\{key_values[i][2]}" "{i}" {parse_var}')