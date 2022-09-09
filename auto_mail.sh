#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2022-05-26 03:18:33 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
python3.8 -mpip uninstall PyQt5
python3.8 -mpip uninstall PyQt5-sip
python3.8 -mpip uninstall PyQtWebEngine
python3.8 -m pip install pyqt5==5.14.0
cd /home/trottar/Programs/my_programs/customsearch/src/
python3.8 auto_mail.py
