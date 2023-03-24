#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2023-03-21 00:33:57 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

import pandas as pd
from datetime import datetime

today = datetime.today()
current_day = today.strftime("%B %d, %Y")

now = datetime.now()
current_hour = int(now.strftime("%H"))
current_min = int(now.strftime("%M"))
current_sec = int(now.strftime("%S"))


if current_min+1 < 60:
    current_time = "{0:02d}:{1:02d}:{2:02d}".format(current_hour,current_min+1,current_sec)
else:
    current_time = "{0:02d}:{1:02d}:{2:02d}".format(current_hour+1,"00","00")
    
print("Email will be sent at", current_time)

import schedule
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os, sys

import rss
from summarize_zotero import summarize_zotero

my_email_addr = os.environ.get('PY_EMAIL')
my_email_pass = os.environ.get('PY_EMAIL_PASS')

# send our email message 'msg' to our boss
def message(subject="Python Notification", 
            text="", img=None, attachment=None):
    
    # build message contents
    msg = MIMEMultipart()
      
    # Add Subject
    msg['Subject'] = subject  
      
    # Add text contents
    msg.attach(MIMEText(text))  
  
    # Check if we have anything
    # given in the img parameter
    if img is not None:
  
          # Check whether we have the
        # lists of images or not!
        if type(img) is not list:
            
              # if it isn't a list, make it one
            img = [img]  
  
        # Now iterate through our list
        for one_img in img:
            
              # read the image binary data
            img_data = open(one_img, 'rb').read()  
              
            # Attach the image data to MIMEMultipart
            # using MIMEImage,
            # we add the given filename use os.basename
            msg.attach(MIMEImage(img_data, 
                                 name=os.path.basename(one_img)))
  
    # We do the same for attachments
    # as we did for images
    if attachment is not None:
  
          # Check whether we have the
        # lists of attachments or not!
        if type(attachment) is not list:
            
              # if it isn't a list, make it one
            attachment = [attachment]  
  
        for one_attachment in attachment:
  
            with open(one_attachment, 'rb') as f:
                
                # Read in the attachment using MIMEApplication
                file = MIMEApplication(
                    f.read(),
                    name=os.path.basename(one_attachment)
                )
            file['Content-Disposition'] = f'attachment;\
            filename="{os.path.basename(one_attachment)}"'
              
            # At last, Add the attachment to our message object
            msg.attach(file)
    return msg
  
  
def mail():
    
    # initialize connection to our email server,
    # we will use gmail here
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
      
    # Login with your email and password
    smtp.login(my_email_addr, my_email_pass)

    # Need to grab summary and title (plus URL?) from here
    art_info = summarize_zotero()


    print(f'\n\n\n{art_info}')
    
    # Find and grab random article from Must Read
    art_title = art_info[0]
    art_sum = art_info[1]
    art_link = art_info[2]
    if art_sum == None:
        art_body = "{0}\n {2} | URL:{1}".format('-'*70,art_link,art_title)
    else:
        art_body = "{0}\n\t{3}\n\n{2} | URL:{1}".format('-'*70,art_link,art_title,art_sum)
    
    # Archive articles
    arxiv_body = ""
    for i,row in rss.import_rss().iterrows():
        url = row['url']
        url_title = row['title']
        if i == 0:
            arxiv_body += "{0}\n{1}) {3} | URL:{2}".format('-'*70,i+1,url,url_title)
        else:
            arxiv_body += "\n{0}) {2} | URL:{1}".format(i+1,url,url_title)

    # Call the message function
    msg = message("Login Email, {0} at {1}".format(current_day,current_time), "Article of the Day\n{1}\n{0}\n\n\narXiv RSS...\n{2}\n{0}".format('-'*70,art_body,arxiv_body))
      
    # Make a list of emails, where you wanna send mail
    to = [os.environ.get('PY_EMAIL_CUA')]
  
    # Provide some data to the sendmail function!
    smtp.sendmail(from_addr=os.environ.get('PY_EMAIL_CUA'),
                  to_addrs=to, msg=msg.as_string())
      
    # Finally, don't forget to close the connection
    smtp.quit()

#schedule.every(10).seconds.do(mail)    
schedule.every().day.at(current_time).do(mail)

def get_job_time(now):
    job_hour = int(now.strftime("%H"))
    job_min = int(now.strftime("%M"))
    job_sec = int(now.strftime("%S"))
    job_time = "{0:02d}:{1:02d}:{2:02d}".format(job_hour,job_min,job_sec)
    return job_time

while True:
    now = datetime.now()
    job_time = get_job_time(now)
    schedule.run_pending()
    time.sleep(1)
    if job_time == current_time:
        print("\n\n",job_time,"=",current_time)
        break

