#! /bin/bash

#
# Description: Upgrade all python packages with pip
# ================================================================
# Time-stamp: "2023-10-17 14:27:38 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

echo "Updating Python..."
python ~/bin/python/upgradePython.py

echo
echo
echo "Updating Python3.8..."
python3.8 ~/bin/python/upgradePython.py 
