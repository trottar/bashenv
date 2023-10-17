#!/usr/bin/tcsh

hostname | tr -d '\n';echo -n "@";hostname -I

