#!/usr/bin/python
import time
import M2MConnect
import M2MSendCommand

def get(ser, address):
    ret = M2MSendCommand.sendCommand("AT+CGDCONT?\r\n", ser)
    print "AT+CGDCONT"
    print ret
    time.sleep(2)
  
    while True:
        ret = M2MSendCommand.sendCommand('AT+UHTTP=0,1,' + address + '\r\n', ser)
        print "AT+UHTTP"
        print ret
        time.sleep(2)
        ret = ser.write('AT+UHTTPC=0,1,"/","r"\r\n')
        print "AT+UHTTPC"
        print ret
        time.sleep(2)
        ret = ser.write('AT+URDFILE="r"\r\n')
        print "AT+URDFILE"
        print ret
        time.sleep(2)
        ret = M2MSendCommand.sendCommand("AT\r\n", ser)
        print "AT"
        print ret
        time.sleep(6)
        return True
