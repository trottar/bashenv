#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2023-03-16 16:51:48 trottar"
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


note_text = [f'''
#+OPTIONS: ^:nil
#+TITLE: Notes from {title_text} meeting ({date_string})
#+AUTHOR: Richard L. Trotta III
#+EMAIL: trotta@cua.edu
#+LATEX_CLASS: book


''']

# Keep track of the last user input
last_user_input = ""

print("\033[36m","-"*50,"\033[0m")
print(f"\n\n\033[36mNotes from {title_text} meeting ({date_string})\033[0m\n\n")

while True:

    #user_inp =  input('\033[36m->\033[0m ')
    print("\n\033[36m","-"*50,"\033[0m\n")
    # Read a very long input from the user
    user_inp = sys.stdin.readline().strip()

    # Returns previous prompt if up arrow is pressed
    if user_inp == "\033[A":
        user_inp = last_user_input
        print(user_inp)
    else:
        last_user_input = user_inp

    if user_inp[0:3] == "bye" or user_inp[0:4] == "exit":
        break

    if "* " in user_inp:
        new_bullet = f"*{user_inp}\n"
    if "- " in user_inp:
        new_bullet = f"{user_inp}\n"
    else:
        new_bullet = f"* {user_inp}\n"
    
    note_text.append(new_bullet)

    
# Check if input given
if len(note_text) > 1:    
    with open(f_name, "w") as f:
        f.write("".join(note_text))
