#!/usr/local/python34/bin/python3.4
# -*- coding: utf-8 -*-
'''
Created on 2015-09-09
Author: xiaohanfei
'''
import os
import datetime
import time
import configparser
import re
import logging
import traceback

def logs(logName):
    logger = logging.getLogger()
    handler = logging.FileHandler('/data/python/logs/'+logName)
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    return logger

def GetConfig():
    config = configparser.ConfigParser()
    config.read("whiteList.conf")
    branchName_wl = config.get("branchName_wl","wl_1")
    return branchName_wl

def getMasterTime(dir):
    os.chdir(dir)
    tmp = os.popen('git log --stat -1').readlines()
    print(tmp)
    tmp1 = tmp[3].split(':   ')
    tmp2 = tmp1[1].split(' +')
    struct_time = time.strptime(tmp2[0])
    masterTime = time.mktime(struct_time)
    return masterTime

def getbranchTime(dir):
    os.chdir(dir)
    branchInfo = os.popen('git branch -a |grep \'examination\'').readlines()
    for i in branchInfo:
        branchName = i
        branchName = list(branchName)
        del branchName[-1]
        branchName = ('').join(branchName)
        command = 'git log'+branchName+' --grep=^Merge -1'
        command2 = 'git log'+branchName+' -1'
        str = os.popen(command).readlines()
        author = os.popen(command2).readlines()

        for a in author:
            if a.find("Author"):
               continue
            else:
               branchAuthor = a
        str1 = str[3].split(':   ')
        if len(str1) == 1:
          continue

        str2 = str1[1].split(' +')
        #print(len(str2))
        struct_time = time.strptime(str2[0])
        branchTime = time.mktime(struct_time)
        branchData = {'branchAuthor':branchAuthor,'branchTime': branchTime,'branchName':branchName}
        if float(masterTime) <= float(branchData['branchTime']) + float('3600'):
           continue
        elif(float(masterTime)-float(branchData['branchTime']) >= float('432000')):
          #print('\033[1;31;40m')
          #f = open('./branchInfo.log','r+')
          result = branchAuthor+"的测试分支"+branchData['branchName']+"超过一周没有合并最新主干,请及时合并"+"\n"+"该分支最后一次合并master的时间为："+time.asctime(time.localtime(branchData['branchTime']))
          logger.info(result)
          #f.write(Result)
          #f.close()
        else:
           #print(branchData['branchName'])
          result2 = branchAuthor+"的测试分支"+branchData['branchName']+"没有合并最新主干,请及时合并"+"\n"+"该分支最后一次合并master的时间为："+time.asctime(time.localtime(branchData['branchTime']))
          logger.info(result2)
if __name__ == "__main__":
 f = open('/data/python/logs/error.log','w')
 try:
  logName = 'git_checkInfo.log'
  if os.path.exists('/data/python/logs/'+logName):
     os.remove('/data/python/logs/'+logName)
       
  os.system('python /data/python/updateMaster.py')
  app = ['pc','wap','admin']
  logger = logs(logName)
  for i in app:
    dir = "/data/httpd/game/"+i
    masterTime = getMasterTime(dir)
    result = "\n"+"["+i+"]当前master最后一次合并主干时间为："+time.asctime(time.localtime(masterTime))+"\n"+"以下测试分支没有合并主干请及时合并，若已上线或作废，请及时清理！"
    logger.info(result)
    getbranchTime(dir)
 except Exception as e:
  errorLogName = '/data/python/logs/error.log'
  log_format = '%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s'
  logging.basicConfig(filename = errorLogName,filemode = 'w',format = log_format,datefmt = '%Y-%m-%d %H:%M:%S %p',level = logging.DEBUG )
  logging.debug(e)

