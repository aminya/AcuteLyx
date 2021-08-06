import os
import shutil
import src.installation.find_lyx as find_lyx
import src.installation.utils.src as p


ui_path = os.path.join(find_lyx.lyx_path, "Resources", "ui")

usertoolbars_src = os.path.join(
    p.src_path, "Resources", "ui", "usertoolbars.inc")
usertoolbars = os.path.join(ui_path, "usertoolbars.inc")
usertoolbars_back = usertoolbars + ".back"
usertoolbars_olderback = usertoolbars + ".olderback"

default_ui = os.path.join(ui_path, "default.ui")
default_ui_back = default_ui + ".back"
default_ui_olderback = default_ui + ".olderback"


def add_user_toolbar():
    print("Installing the user toolbar...")

    print(f"Creating backup files at {default_ui} in case of an error")

    # check if the usertoolbar is added to the settings
    shouldAddUserToolbar = False
    txt: str
    with open(default_ui, "rt") as file:
        txt = file.read()
        if (txt.find('"user" "on,top"') == -1):
            if os.path.isfile(default_ui_back):
                # keep two backups
                shutil.copy(default_ui_back, default_ui_olderback)
                os.remove(default_ui_back)
            shutil.copy(default_ui, default_ui_back)
            txt = txt.replace('Toolbars\n\t"standard" "on,top"',
                              'Toolbars\n\t"standard" "on,top"\n\t"user" "on,top"')
            shouldAddUserToolbar = True
        else:
            print(
                f"The user toolbar already added to the settings at {default_ui}")

    if shouldAddUserToolbar:
        with open(default_ui, "wt") as file:
            # add toolbar to the settings
            file.write(txt)
            print(f"Added the user toolbar to the settings at {default_ui}")

    # keep two backups
    if os.path.isfile(usertoolbars_back):
        shutil.copy(usertoolbars_back, usertoolbars_olderback)
        os.remove(usertoolbars_back)

    # copy usertoolbars
    if os.path.isfile(usertoolbars):
        shutil.copy(usertoolbars, usertoolbars_back)
        os.remove(usertoolbars)
    shutil.copy(usertoolbars_src, usertoolbars)

    print(f"""Installed the user toolbar at {usertoolbars}
    If you want to modify the tooblar, change {usertoolbars_src}, and rerun this script""")


def remove_user_toolbar():
    print("Uninstalling the user toolbar...")

    shouldAddUserToolbar = False
    txt: str
    with open(default_ui, "rt") as file:
        txt = file.read()
        if (txt.find('"user" "on,top"') != -1):
            txt = txt.replace('Toolbars\n\t"standard" "on,top"\n\t"user" "on,top"',
                              'Toolbars\n\t"standard" "on,top"')
            shouldAddUserToolbar = True
        else:
            print("The user toolbar is not added to the settings")

    if shouldAddUserToolbar:
        with open(default_ui, "wt") as file:
            # add toolbar to the settings
            file.write(txt)
            print(
                f"Removed the user toolbar from the settings at {default_ui}")

    if os.path.isfile(usertoolbars):
        os.remove(usertoolbars)

    print(f"Uninstalled the user toolbar at {usertoolbars}")
