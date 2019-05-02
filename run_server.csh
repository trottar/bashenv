#!/usr/bin/bash

# start,restart,stop
eval "sudo service ssh $1"
eval "sudo service ssh status"
