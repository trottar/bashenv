#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2020-01-29 18:57:43 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

SHAREDFILE=$1

eval 'google-chrome http://127.0.0.1:8888/'

eval 'sudo docker run --rm -it -p 8888:8888 -v $SHAREDFILE:/home/eicuser/epw/share eicdev/epic'
