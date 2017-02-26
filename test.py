#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015-9-28

@author: xiaohanfei
'''

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#创建一个带附件的实例
msg = MIMEMultipart()

#构造附件1
att1 = MIMEText(open('/data/python/script/game_line.py', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="game_line.py"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

#构造附件2
att2 = MIMEText(open('/data/python/script/game_line.py', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="abc.py"'
msg.attach(att2)

#加邮件头
msg['to'] = 'vanglis@163.com'
msg['from'] = 'vanglis@163.com'
msg['subject'] = 'hello world'
#发送邮件
server = smtplib.SMTP('smtp.163.com',465)
server.connect('smtp.163.com')
server.login('vanglis@163.com','fei3.14159')#XXX为用户名，XXXXX为密码
server.sendmail(msg['from'], msg['to'],msg.as_string())
server.quit()
print('发送成功')

