#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2021-10-02 01:41:47 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

IFS=$'\n' read -r -d '' -a GITLIST < <( find ~/ -name ".git" && printf '\0' )

for e in "${GITLIST[@]}"; do
    DIR=$( echo "${e}" | sed -e "s/\.git//" )
    cd $DIR
    if [[ `git status --porcelain` ]]; then
	# Changes
	echo "Changes in ${DIR}"
    fi
done
