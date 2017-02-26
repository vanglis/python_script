#!/usr/bin/env python3
#-*-coding:utf-8-*-

from socketIO_client import SocketIO, LoggingNamespace

def on_aaa_response(*args):
    print('on_aaa_response', args)

socketIO = SocketIO('122.224.97.150', 9655, LoggingNamespace)

# Listen
socketIO.on('aaa_response', on_aaa_response)
socketIO.emit('aaa')
socketIO.emit('aaa')
socketIO.wait(seconds=1)

