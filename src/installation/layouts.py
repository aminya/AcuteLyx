import src.installation.find_lyx as find_lyx
import src.installation.utils.src as p
import os
import shutil


def add_layouts():
    print("Installing the user layouts...")

    layouts = os.path.join(find_lyx.lyx_data_path, "layouts")
    layouts_src = os.path.join(p.src_path, "layouts")

    layouts_src_content = os.listdir(layouts_src)
    layouts_content = os.listdir(layouts)
    for file in layouts_src_content:
        if file in layouts_content:
            filepath = os.path.join(layouts, file)
            filepath_src = os.path.join(layouts_src, file)
            filepath_back = filepath + ".back"
            filepath_olderback = filepath + ".olderback"
            if os.path.isfile(filepath_back):
                shutil.copy(filepath_back, filepath_olderback)
                os.remove(filepath_back)
            shutil.copy(filepath, filepath_back)
            shutil.copy(filepath_src, filepath)

    print(f"""Installed the user layouts at {layouts}
    If you want to modify the layouts, change {layouts_src}, and rerun this script""")

