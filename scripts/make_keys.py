import os
import sys
import winreg as reg

# Get path of current working directory and python.exe
cwd = os.getcwd()
python_exe = sys.executable

hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"
parse_var = f'"%1"'

key_values = [(r'*\\shell\\CopyServer\\', '&Copy to server', 'copy_to_server.py'),
              (r'*\\shell\\CopyLocal\\', '&Copy to local', 'copy_to_local.py'),
              (r'*\\shell\\CopyOverwriteServer\\', '&Copy/Overwrite to server', 'overwrite_to_server.py'),
              (r'*\\shell\\CopyOverwriteLocal\\', '&Copy/Overwrite to local', 'overwrite_to_local.py'),
             ]

for key_value in key_values:
    key_path = key_value[0]
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
    reg.SetValue(key, '', reg.REG_SZ, key_value[1])
    reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, f'{cwd}\\icon.ico')
    key_cmd = reg.CreateKey(key, r"command")
    reg.SetValue(key_cmd, '', reg.REG_SZ, python_exe + f' "{cwd}\\scripts\\{key_value[2]}" {parse_var}' )
    reg.SetValue(key_cmd, '', reg.REG_SZ, hidden_terminal + f' "{cwd}\\scripts\\{key_value[2]}" {parse_var}' )