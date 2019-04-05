#!/usr/bin/bash

while true; do
    read -p "Are you retrieving a file? (Please answer yes or no) " yn
    case $yn in
	[Yy]* )
	    read -p "Which type of file would you like to import? (scratch or not): " TYPE
	    if [ $TYPE = "scratch" ]; then
		read -p "What file in scratch would you like to recieve?: " FILE
		read -p "Where would you like the file to go?: " LOCATION
		eval "scp trottar@login.jlab.org:~/../../scratch/trottar/$FILE $LOCATION"
	    else
		echo "Type $TYPE not found..."
		echo
		echo
		echo "Going to home directory..."
		echo
		echo
		read -p "Which file would you like to import?: " FILE
		read -p "Where would you like the file to go?: " LOCATION
		eval "scp trottar@login.jlab.org:~/$FILE $LOCATION"
	    fi
	    break;;
        [Nn]* )
	    read -p "Which file would you like to export?: " FILE
	    read -p "Where would you like the file to go?: " LOCATION
	    eval "scp $FILE trottar@login.jlab.org:$LOCATION"
	    exit;;
        * ) echo "Please answer yes or no.";;	
    esac
done
