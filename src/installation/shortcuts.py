import src.installation.find_lyx as find_lyx
import src.installation.utils.src as p
import os
import shutil


def add_shortcuts():
    print("Installing the user shortcuts...")

    user_bind = os.path.join(find_lyx.lyx_data_path, "bind", "user.bind")
    user_bind_back = user_bind + ".back"
    user_bind_olderback = user_bind_back + ".olderback"
    user_bind_src = os.path.join(p.src_path, "bind", "user.bind")

    # keep two backups
    if os.path.isfile(user_bind_back):
        shutil.copy(user_bind_back, user_bind_olderback)
        os.remove(user_bind_back)

    # copy user.bind
    if os.path.isfile(user_bind):
        shutil.copy(user_bind, user_bind_back)
        os.remove(user_bind)

    shutil.copy(user_bind_src, user_bind)

    print(f"""Installed the user shortcuts at {user_bind}
    If you want to modify the shortcuts, change {user_bind_src}, and re-run this script""")


def remove_shortcuts():
    print("Uninstalling the user shortcuts...")

    user_bind = os.path.join(find_lyx.lyx_data_path, "bind", "user.bind")

    if os.path.isfile(user_bind):
        os.remove(user_bind)

    print(f"Uninstalled the user shortcuts at {user_bind}")
