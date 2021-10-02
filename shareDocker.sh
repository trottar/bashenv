#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2020-05-06 11:46:58 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

SHAREDFILE=$1

eval 'google-chrome http://127.0.0.1:8888/'

eval 'google-chrome http://127.0.0.1:6080/'

eval 'sudo docker run -it -p8888:8888 -p6080:6080  -v $SHAREDFILE:/home/eicuser/epw/share electronioncollider/escalate'
