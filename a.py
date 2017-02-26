#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from ftplib import FTP
import zipfile

def zip_file():
 f = zipfile.ZipFile('test.zip','w',zipfile.ZIP_DEFLATED)
 zipdir = '/data/python/test'
 for dirpath, dirnames, filenames in os.walk(zipdir):
    for filename in filenames:
        f.write(os.path.join(dirpath,filename))
 f.close()


if __name__ == '__main__':
 zip_file()
