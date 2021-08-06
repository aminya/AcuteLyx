import src.installation.shortcuts as sh
import src.installation.layouts as ly
import src.installation.user_toolbar as tb


def main():
    sh.remove_shortcuts()
    ly.remove_layouts()
    tb.remove_user_toolbar()


main()
