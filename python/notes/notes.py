#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2023-03-15 20:09:21 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
import datetime
# Required for up arrow returns
import readline
import os, sys

title_text = "".join(sys.argv[1].split())

# Get the current date and time
now = datetime.datetime.now()
# Format the date and time as a string to use in the file name
date_string = now.strftime("%Y-%m-%d")

home_dir = os.path.expanduser("~")

f_name = f"{home_dir}/Documents/Notes/note_{title_text}_{date_string}.org"


note_text = ['''
#+OPTIONS: ^:nil
#+TITLE: Notes from %s meeting (%s)
#+AUTHOR: Richard L. Trotta III
#+EMAIL: trotta@cua.edu
#+latex_header: \hypersetup{colorlinks=true,linkcolor=blue}
#+LATEX_CLASS: book


''' % (title_text, date_string)]

# Keep track of the last user input
last_user_input = ""

while True:

    user_inp =  input('\033[36m->\033[0m ')

    # Returns previous prompt if up arrow is pressed
    if user_inp == "\033[A":
        user_inp = last_user_input
        print(user_inp)
    else:
        last_user_input = user_inp

    if user_inp[0:3] == "bye" or user_inp[0:4] == "exit":
        break

    if "*" in user_inp:
        new_bullet = f"*{user_inp}\n"
    else:
        new_bullet = f"* {user_inp}\n"
    
    note_text.append(new_bullet)

    

with open(f_name, "w") as f:
    f.write("".join(note_text))
