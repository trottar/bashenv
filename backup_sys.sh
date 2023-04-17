#! /bin/bash

#
# Description:
# ================================================================
# Time-stamp: "2023-04-17 13:38:50 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#


# Get the current date components as separate variables
YEAR=$(date +'%Y')
MONTH=$(date +'%m')
DAY=$(date +'%d')

# External hard drive location
HDDIR="/media/${USER}/extHD"
# Directory to back up system
BACKUPDIR="${HDDIR}/LinuxMintBackup_19-3_Cinnamon/backup_${YEAR}_${MONTH}_${DAY}"


# Check if the directory exists
if [ -d "${HDDIR}" ]; then
    echo
    echo "Backing up system to ${BACKUPDIR}..."
    echo
    echo
    echo
    # This command will copy all files and directories from the root directory to the backup directory on the external hard drive. 
    # The --exclude option is used to exclude certain directories that don't need to be backed up.
    sudo rsync -aAXv /* $BACKUPDIR --exclude={/dev/*,/proc/*,/sys/*,/tmp/*,/run/*,/mnt/*,/media/*,/lost+found}    
else
    echo
    echo "${HDDIR} not available. Check HD is plugged in and mounted..."
    echo
    echo
    echo
fi
