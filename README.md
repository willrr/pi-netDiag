# pi-networkDiagnostics
Python network diagnotics tool

Built on linux

Requires Tkinter and fping packages;

sudo apt-get install python3-tk fping

Raspbian Install Guide:

sudo apt-get install python3-tk fping

vim /home/pi/pi-networkDiagnostics/launcher.sh

#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home
cd /
cd home/pi/pi-networkDiagnostics
python3 willrr.py
cd /

vim /home/pi/.config/lxsession/LXDE-pi/autostart

before @xscreensaver:

@/home/pi/pi-networkDiagnostics/launcher.sh
