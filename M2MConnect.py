#!/usr/bin/python
import time
import M2MSendCommand

def connect(ser):
    ret = M2MSendCommand.sendCommand("AT\r\n", ser)
    print "AT"
    print ret
    time.sleep(2)
    ret = M2MSendCommand.sendCommand("AT+CFUN=1,1", ser)
    print "AT+CFUN=1,1"
    print ret
    time.sleep(30)
    ret = M2MSendCommand.sendCommand("AT+CEREG=1", ser)
    print "AT+CEREG=1"
    print ret
    time.sleep(2)
    ret = M2MSendCommand.sendCommand("AT+UPSD=0,0,2\r\n", ser)
    print "AT+UPSD=0,0,2"
    print ret
    time.sleep(2)
    ret = M2MSendCommand.sendCommand("AT+UPSDA=0,3\r\n", ser)
    print "AT+UPSDA=0,3"
    print ret
    time.sleep(2)
    return True
