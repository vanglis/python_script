#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

sender = 'vanglis@163.com'
receiver = 'vanglis@163.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'vanglis@163.com'
password = 'fei3.14159'

#msg['Subject'] = 'zhuti'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'send mesg'

#附件
att = MIMEText(open('sq.py','rb').read(),'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="a.py"'
msgRoot.attach(att)


smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
#smtp.quit()
