#!/usr/bin/python
import M2MInit
import M2MConnect

def init():
    ser = M2MInit.init()
    return ser

def connect():
    connected = M2MConnect.connect(ser)
    return connected
