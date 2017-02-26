#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015-11-2

@author: xiaohanfei
'''
import socket

def client(data):
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysocket.connect(('25.17.1.165',9555))
    mysocket.send(data.encode())
    print(mysocket.recv(1024))
    mysocket.close()

if __name__ == '__main__':
   data = input('> ')
   client(data)
    
