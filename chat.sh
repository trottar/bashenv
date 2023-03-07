#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2023-03-06 21:59:13 trottar"
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
	echo "     arg1='Chat prompt type (jlab, root, python, c++, or fortran)"
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

    echo
    echo
    echo "Running chat program for $1 in GUI..."
    echo
    
    python3.8 chatgpt.py $1 "gflag"
    
else

    echo
    echo
    echo "Running chat program for $1 in terminal..."
    echo
    
    python3.8 chatgpt.py $1
    
fi
