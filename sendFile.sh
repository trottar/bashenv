#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2019-04-30 10:35:10 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

ipaddressPC="192.168.1.174"
ipaddressVB="192.168.1.193"

ipaddress=$( eval "hostname -I" )

while true; do
    if [ $ipaddress == $ipaddressPC ]; then
	read -p "Are you retrieving a file? (Please answer yes or no) " yn
	case $yn in
	    [Yy]* )
		read -p "Which file would you like to import?: " FILE
		read -p "Where would you like the file to go?: " LOCATION
		eval "sudo rsync -avzhe ssh --progress trottar@$ipaddressVB:~/$FILE $LOCATION"
		break;;
            [Nn]* )
		read -p "Which file would you like to export?: " FILE
		read -p "Where would you like the file to go?: " LOCATION
		eval "sudo rsync -avzhe ssh --progress $FILE trottar@$ipaddressVB:~/$LOCATION"
		exit;;
            * ) echo "Please answer yes or no.";;	
	esac
    elif [ $ipaddress == $ipaddressVB ]; then
		read -p "Are you retrieving a file? (Please answer yes or no) " yn
	case $yn in
	    [Yy]* )
		read -p "Which file would you like to import?: " FILE
		read -p "Where would you like the file to go?: " LOCATION
		eval "sudo rsync -avzhe ssh --progress trottar@$ipaddressPC:~/$FILE $LOCATION"
		break;;
            [Nn]* )
		read -p "Which file would you like to export?: " FILE
		read -p "Where would you like the file to go?: " LOCATION
		eval "sudo rsync -avzhe ssh --progress $FILE trottar@$ipaddressPC:~/$LOCATION"
		exit;;
            * ) echo "Please answer yes or no.";;	
	esac
    else
	echo "IP address does not match any known"
    fi
done
