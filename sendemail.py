#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = ''
receiver = ''
subject = 'python email test'
smtpserver = ''
username = ''
password = ''
  
msg = MIMEText('你好','text','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
  
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
