#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

sender = 'vanglis@163.com'
receiver = 'vanglis@163.com'
subject = 'python email test'
smtpserver = ''
username = 'vanglis@163.com'
password = 'fei3.14159'

#msg['Subject'] = 'zhuti'
msgs = "#登录信息  "
#附件
msg = MIMEText(msgs,'text','utf-8')
msg['Subject'] = Header(subject,'utf-8')
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
