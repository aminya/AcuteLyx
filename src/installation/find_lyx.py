import glob
import os
import src.installation.utils.platform_detect as pf

lyx_path: str
if pf.is_windows:
    maybe_lyx_path = (glob.glob("C:\\Program Files\\Lyx*") +
                      glob.glob("C:\\Program Files (x86)\\Lyx*"))
    if len(maybe_lyx_path) == 0:
        raise "Lyx installation was not found"
    else:
        lyx_path = maybe_lyx_path[0]

print("Lyx was found in ", lyx_path)

lyx_data_path: str
if pf.is_windows:
    maybe_lyx_data_path = glob.glob(os.getenv("APPDATA") + "/Lyx*")
    if len(maybe_lyx_data_path) == 0:
        raise "Lyx app data was not found"
    else:
        lyx_data_path = maybe_lyx_data_path[0]

print("Lyx app data was found in ", lyx_data_path)
