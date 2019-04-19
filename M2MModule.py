#!/usr/bin/python
import M2MInit
import M2MConnect
import M2MGet

global ser

def init():
    ser = M2MInit.init()
    return ser

def connect(ser):
    connected = M2MConnect.connect(ser)
    return connected

def get(ser, address):
    return M2MGet.get(ser, address)
