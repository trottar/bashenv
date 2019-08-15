#! /usr/bin/python

#
# Description: Upgrade all python packages with pip
# ================================================================
# Time-stamp: "2019-08-14 14:59:11 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#


import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
