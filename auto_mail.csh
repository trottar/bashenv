#! /bin/tcsh

#
# Description:
# ================================================================
# Time-stamp: "2023-10-13 15:12:21 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

source $HOME/.cshrc

cd $HOME/bin/python/gmail/
python3.8 auto_mail.py
cd $HOME/bin/text_files/
rm -f *.pdf
rm -f *.txt
