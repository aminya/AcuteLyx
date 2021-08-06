# AcuteLyx (AcuteLatex)

A collection of environments, shortcuts, toolbars, packages, etc. to enhance [Lyx](https://www.lyx.org/Download#toc3).

# Installation

Open terminal as Administrator and run the following command. Then from the Lyx Toolbar select `Tools > Reconfigure`. When reconfiguration is done, hit OK, and restart Lyx.
```
python ./installation.py
```

**Node: the installation script is only tested on Windows.** Pull requests for supporting other OS are welcome.

# Lyx Shortcuts

## Normal mode:

Description                                | Shortcut
-------------------------------------------|---------
add a new section/environment              | `ALT-S`
add label (for figures, equations, etc.)   | `ALT-M`
add citation                               | `ALT-C`
add a reference to a figure/table/equation | `ALT-R`
add hyperlink                              | `ALT-H`
layout-paragraph                           | `CTRL-P`
dialog-show character                      | `CTRL-T`

## Math mode:

Description              | Shortcut
-------------------------|---------------
inline math              | `CTRL+M`
standalone math          | `CTRL+SHIFT+M`
numbered math            | `CTRL+ALT+N`
convert to numbered math | `CTRL+ALT+M`
text in math (\\mbox)    | `ALT-T`
fractions (\\frac)       | `ALT-F`
brackets                 | `ALT+M+[,{,(`

# Uninstallation

Open terminal as Administrator and run the following command. Then from the Lyx Toolbar select `Tools > Reconfigure`. When reconfiguration is done, hit OK, and restart Lyx.
```
python ./uninstallation.py
```
