#!/usr/bin/bash

set GROUP=$1

set DIRGROUP=/group/c-kaonlt
set DIRHOME=/group/c-kaonlt/USERS/$USER/hallc_replay_kaonlt/

if ( $1 == "group" ) then
    echo "Going to $DIRGROUP"
    cd $DIRGROUP
else if ( $1 == "home" ) then
    echo "Going to $DIRHOME"
    cd $DIRHOME
else
    echo "Invalid entry"
    echo $?
endif 
