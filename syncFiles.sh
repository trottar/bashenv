#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2019-04-29 23:16:19 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

ipaddressPC="192.168.1.174"
ipaddressVB="192.168.1.193"

ipaddress=$( eval "hostname -I" )

echo "$ipaddress"
echo "$ipaddressPC PC"
echo "$ipaddressVB VB"

while true; do
    read -p "Would you like to send to remote connection? (Please answer yes or no) " yn
    case $yn in
        [Yy]* )
	    if [ $ipaddress == $ipaddressPC ]; then
		echo
		echo "Syncing PC with VB"
		echo
		echo "Syncing opt"
		sudo rsync -avzhe ssh --progress /opt/* trottar@$ipaddressVB:/opt/ 
		
		echo "Syncing home"
		sudo rsync -avzhe ssh --progress ~/* trottar@$ipaddressVB:~/
		# sudo rsync -avzhe ssh --progress ~/.* trottar@$ipaddressVB:~/
	    elif [ $ipaddress == $ipaddressVB ]; then
		echo
		echo "Syncing VB with PC"
		echo
		echo "Syncing opt"
		sudo rsync -avzhe ssh --progress /opt/* trottar@$ipaddressPC:/opt/ 
		
		echo "Syncing home"
		sudo rsync -avzhe ssh --progress ~/* trottar@$ipaddressPC:~/
		# sudo rsync -avzhe ssh --progress ~/.* trottar@$ipaddressPC:~/
	    else
		echo "IP address does not match any known"
	    fi

	    break;;
        [Nn]* )
	    echo "Syncing from external harddrive"
	    ########################
	    # No need to copy this #
	    ########################
	    # echo "Syncing etc"
	    # sudo rsync -avzhP /media/trottar/Seagate\ Backup\ Plus\ Drive/MintLaptop/etc/* /etc/
	    # pkexec chown root:root /etc/sudoers /etc/sudoers.d -R 
	    # eval "sudo update-grub"
	    # eval "sudo grub-mkconfig -o /boot/grub/grub.cfg"

	    echo "Syncing opt"
	    sudo rsync -avzhP /media/trottar/Seagate\ Backup\ Plus\ Drive/MintLaptop/opt/* /opt/

	    echo "Syncing home"
	    sudo rsync -avzhP /media/trottar/Seagate\ Backup\ Plus\ Drive/MintLaptop/home/trottar/* ~/
	    sudo rsync -avzhP /media/trottar/Seagate\ Backup\ Plus\ Drive/MintLaptop/home/trottar/.* ~/

	    echo "Changing permissions of directories"
	    find ~/ -type d -exec chmod o-rwx {} +
	    find ~/ -type d -exec chmod a+rwx {} +

	    echo "Changing permissions of files (executables will need to be changed again)"
	    find ~/ -type f -exec chmod a-rwx {} +
	    find ~/ -type f -exec chmod a+rw {} +

	    echo "Getting packages"
	    sudo apt-get update && cat pkglist | xargs sudo apt-get install -y

	    exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
