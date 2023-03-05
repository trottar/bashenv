#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2023-03-05 04:19:14 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

# Flag definitions (flags: hg)
while getopts 'hg' flag; do
    case "${flag}" in
        h) 
        echo "--------------------------------------------------------------"
        echo "./chat.sh -{flags}"
	echo
        echo "Description: Run ChatGPT in terminal or GUI."
        echo "--------------------------------------------------------------"
        echo
        echo "The following flags can be called for the heep analysis..."
        echo "    -h, help"
	echo "    -g, gui"
        exit 0
        ;;
	g) g_flag='true' ;;
        *) print_usage
        exit 1 ;;
    esac
done

cd ~/bin/python/gpt/

if [[ $g_flag = "true" ]]; then    

    python3.8 chatgpt.py "gflag"
    
else

    python3.8 chatgpt.py
    
fi
