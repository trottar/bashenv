#!/usr/bin/bash

while true; do
    read -p "Are you retrieving a file? (Please answer yes or no) " yn
    case $yn in
	[Yy]* )
	    read -p "Which file would you like to import from /volatile?: " FILE
	    read -p "Where would you like the file to go?: " LOCATION
	    # eval "scp trottar@login.jlab.org:/w/hallc-scifs17exp/kaon/trottar/hallc_replay/ROOTfiles/$FILE $LOCATION"
	    eval "scp trottar@scigw.jlab.org:/lustre/expphy/volatile/hallc/spring17/trottar/ROOTfiles/$FILE $LOCATION"
	    break;;
        [Nn]* )
	    read -p "Which file would you like to export to /volatile?: " FILE
	    read -p "Where would you like the file to go?: " LOCATION
	    # eval "scp $FILE trottar@login.jlab.org:/w/hallc-scifs17exp/kaon/trottar/$LOCATION"
	    eval "scp $FILE trottar@scigw.jlab.org:/lustre/expphy/volatile/hallc/spring17/trottar/ROOTfiles/$LOCATION"
	    exit;;
        * ) echo "Please answer yes or no.";;	
    esac
done
