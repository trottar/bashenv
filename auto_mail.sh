#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2023-03-21 00:40:10 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

#python3.8 -mpip uninstall -y PyQt5
#python3.8 -mpip uninstall -y PyQt5-sip
#python3.8 -mpip uninstall -y PyQtWebEngine
#python3.8 -m pip install -y pyqt5==5.14.0
cd python/gmail/
python3.8 auto_mail.py
cd text_files/
rm -f *.pdf
rm -f *.txt
