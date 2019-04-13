#!/usr/bin/bash

while true; do
    read -p "Are you retrieving a file? (Please answer yes or no) " yn
    case $yn in
	[Yy]* )
	    read -p "Which file would you like to import from /work?: " FILE
	    read -p "Where would you like the file to go?: " LOCATION
	    eval "scp trottar@login.jlab.org:/w/hallc-scifs17exp/kaon/trottar/hallc_replay/ROOTfiles/$FILE $LOCATION"
	    break;;
        [Nn]* )
	    read -p "Which file would you like to export to /work?: " FILE
	    read -p "Where would you like the file to go?: " LOCATION
	    eval "scp $FILE trottar@login.jlab.org:/w/hallc-scifs17exp/kaon/trottar/$LOCATION"
	    exit;;
        * ) echo "Please answer yes or no.";;	
    esac
done
