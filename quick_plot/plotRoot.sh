#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2020-01-30 22:37:32 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

read -p "Please enter a leaf name..." LEAFNAME

if [[ LEAFNAME -eq "" ]]; then

    echo "No leaf name was entered..."
    
    read -p "Which root file would you like to plot? " ROOTNAME

    read -p "Is that located in your current directory? (Please answer yes or no) " yn
    case $yn in
	[Yy]* )
	    DIR=$(echo "$PWD")
	    read -p "Which tree? " TREENAME
	    break;;
	[Nn]* )
	    read -p "Where is the root file located? " DIR
	    read -p "Which tree? " TREENAME
    esac	  
    python $HOME/bin/quick_plot/checkTBrowser.py "$DIR/$ROOTNAME" $TREENAME
    read -p "Please reenter a leaf name..." LEAFNAME
else

read -p "Which root file would you like to plot? " ROOTNAME

read -p "Is that located in your current directory? (Please answer yes or no) " yn
case $yn in
    [Yy]* )
	DIR=$(echo "$PWD")
	read -p "Which tree? " TREENAME
	break;;
    [Nn]* )
	read -p "Where is the root file located? " DIR
	read -p "Which tree? " TREENAME
esac

fi

echo "Plotting $LEAFNAME in tree $TREENAME located in $DIR/$ROOTNAME"
echo " |"
echo " |"
echo " v"

python $HOME/bin/quick_plot/plotRoot.py "$DIR/$ROOTNAME" $TREENAME $LEAFNAME
