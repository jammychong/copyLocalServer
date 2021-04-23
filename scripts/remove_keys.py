from winreg import *

keys = ["CopyLocal", "CopyServer", "CopyOverwriteLocal", "CopyOverwriteServer"]

for key in keys:
    try:
        key_path = "*\\shell\\{}".format(key)
        open_key = OpenKey(HKEY_CLASSES_ROOT, key_path, 0, KEY_ALL_ACCESS)
        subkey = EnumKey(open_key, 0)
        DeleteKey(open_key, subkey)
        DeleteKey(HKEY_CLASSES_ROOT, key_path)
    except:
        pass