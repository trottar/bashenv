#! /bin/tcsh

#
# Description:
# ================================================================
# Time-stamp: "2023-10-17 01:45:03 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

source $HOME/.cshrc

# Check if the last run file exists
if (-e $HOME/bin/log/syncthunderbird.log) then
    # Get the timestamp of the last run
    set last_run = `cat $HOME/bin/log/syncthunderbird.log`

    # Get the current timestamp
    set current_time = `date +%s`

    # Calculate the time difference in seconds
    set time_difference = `expr $current_time - $last_run`

    # Calculate the time difference in days
    set time_difference_days = `expr $time_difference / 86400`

    # Check if it has been 7 days or more
    if ($time_difference_days >= 7) then
        # Update the last run timestamp
        echo $current_time > $HOME/bin/log/syncthunderbird.log

	# Explanation of options:
	# -a: Archive mode (preserves permissions, ownership, timestamps, etc.)
	# -v: Verbose mode (shows detailed output, helpful for debugging)
	# -z: Compress file data during the transfer (reduces network usage)
	# --update: Skip files that are newer on the receiver
	# --ignore-existing: Skip updating files that already exist in the destination
	rsync -avz -e "ssh -A -i $HOME/.ssh/id_rsa" --update trottar@PC:/mnt/c/Users/papatrott/AppData/Roaming/Thunderbird/ $HOME/.thunderbird/    
    endif
else
    # If last run file doesn't exist, create it and set the current timestamp
    echo `date +%s` > $HOME/bin/log/syncthunderbird.log

    # Explanation of options:
    # -a: Archive mode (preserves permissions, ownership, timestamps, etc.)
    # -v: Verbose mode (shows detailed output, helpful for debugging)
    # -z: Compress file data during the transfer (reduces network usage)
    # --update: Skip files that are newer on the receiver
    # --ignore-existing: Skip updating files that already exist in the destination
    rsync -avz -e "ssh -A -i $HOME/.ssh/id_rsa" --update trottar@PC:/mnt/c/Users/papatrott/AppData/Roaming/Thunderbird/ $HOME/.thunderbird/    
endif
