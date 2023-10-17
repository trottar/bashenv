#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2023-09-11 22:05:49 trottar"
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
import subprocess

title_text = "".join(sys.argv[1].split())

# Get the current date and time
now = datetime.datetime.now()
# Format the date and time as a string to use in the file name
date_string = now.strftime("%Y-%m-%d")
formatted_date = now.strftime("%Y %b %d")

home_dir = os.path.expanduser("~")

f_name = f"{home_dir}/Documents/Notes/note_{title_text}_{date_string}.org"

# toc:nil (ignore table of contents), H:0 (ignore underlines in *.txt), num:nil (ignore section numbers in *.txt)
note_text = [f'''
#+OPTIONS: ^:nil toc:nil H:0 num:nil
#+TITLE: {formatted_date} (Notes from {title_text} meeting)
#+AUTHOR: Richard L. Trotta III
#+EMAIL: trotta@cua.edu
#+LATEX_CLASS: book


''']

# Keep track of the last user input
last_user_input = ""

print("\033[36m","-"*50,"\033[0m")
print(f"\n\n\033[36mNotes from {title_text} meeting ({formatted_date})\033[0m\n\n")

while True:

    print("\n\033[36m","-"*50,"\033[0m\n")
    #user_inp =  input('\033[36m->\033[0m ')
    user_inp = input()
    # Read a very long input from the user
    #user_inp = sys.stdin.readline().strip()

    # Returns previous prompt if up arrow is pressed
    if user_inp == "\033[A":
        user_inp = last_user_input
        print(user_inp)
    else:
        last_user_input = user_inp

    if user_inp[0:3] == "bye" or user_inp[0:4] == "exit":
        print("\n\033[36m","-"*50,"\033[0m\n")
        break
    if user_inp == "":
        continue

    if user_inp.lower() == "save":  # Check if the user typed "save"
        with open(f_name, "w") as f:
            f.write("".join(note_text))
        print(f"\n\033[36mFile '{f_name}' saved successfully!\033[0m\n")
        continue
    
    if user_inp[0:6] == "delete":
        pop_ele = note_text.pop()
        print(f"\n\033[36m{pop_ele} deleted...\033[0m\n")
        continue
    if user_inp[0:7] == "summary":
        for bullet in note_text:
            print(f"\n\033[36m{bullet}\033[0m\n")
        continue
    
    if "* " in user_inp:
        new_bullet = f"*{user_inp}\n"
    elif "- " in user_inp:
        new_bullet = f"{user_inp}\n"
    else:
        new_bullet = f"* {user_inp}\n"
    
    note_text.append(new_bullet)

    
# Check if input given
if len(note_text) > 1:
    with open(f_name, "w") as f:
        f.write("".join(note_text))

# run the aspell command on the text file
#result = subprocess.run(['aspell', '-c', f_name], capture_output=True, text=True)
result = subprocess.run(['aspell', '-c', f_name])

print("\n\nSpell check complete!")

f_name_txt = f_name.replace(".org",".txt")

# Initialize variables to store information
title = ""
author = ""
email = ""
content = ""

# Read the Org mode file
with open(f_name, 'r', encoding='utf-8') as org_file:
    lines = org_file.readlines()

# Extract information from the Org mode file
for line in lines:
    if line.startswith("#+TITLE:"):
        title = line.strip().split(": ")[1]
    elif line.startswith("#+AUTHOR:"):
        author = line.strip().split(": ")[1]
    elif line.startswith("#+EMAIL:"):
        email = line.strip().split(": ")[1]
    elif not line.startswith("#"):
        content += line

# Write the content to a UTF-8 text file
with open(f_name_txt, 'w', encoding='utf-8') as output_file:
    output_file.write(f"{title}\n")
    output_file.write(f"{author}\n")
    output_file.write(f"{email}\n")
    output_file.write(content)

print(f'\n\nOrg mode file converted to {f_name_txt}')

print('\n\n')
print('-'*25)
print('Sending note to Evernote...')

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

my_email_addr = os.environ.get('PY_EMAIL')
my_email_pass = os.environ.get('PY_EMAIL_PASS')

# send our email message 'msg' to our boss
def message(subject=f"{title} @Misc Work #notes", 
            text=f'---\n{title}\n---\n'+content):
    
    # build message contents
    msg = MIMEMultipart()
      
    # Add Subject
    msg['Subject'] = subject  
      
    # Add text contents
    msg.attach(MIMEText(text))
  
    return msg  
  
def mail():
    
    # initialize connection to our email server,
    # we will use gmail here
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
      
    # Login with your email and password
    smtp.login(my_email_addr, my_email_pass)

    # Call the message function
    msg = message()
      
    # Make a list of emails, where you wanna send mail
    to = [os.environ.get('PY_EMAIL_EVERNOTE')]
  
    # Provide some data to the sendmail function!
    smtp.sendmail(from_addr=os.environ.get('PY_EMAIL'),
                  to_addrs=to, msg=msg.as_string())
      
    # Finally, don't forget to close the connection
    smtp.quit()

mail()

print('...note received!')
print('-'*25)
