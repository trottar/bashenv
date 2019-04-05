#!/usr/bin/bash

hostname | tr -d '\n';echo -n "@";hostname -I

