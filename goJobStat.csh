#!/bin/tcsh

set JOBINPUT=$1
set JOBDIR="/lustre/expphy/farm_out/${USER}/"

if ( $1 == "status" ) then
    jobstat -u ${USER}
else if ( $1 == "kill" ) then
    jkill 0
else if ( $1 == "error" ) then
    echo $JOBDIR
    ls -ltr $JOBDIR
else
    echo "Invalid Entry: $1"
    exit
endif
