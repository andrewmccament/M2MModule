#!/usr/bin/python
import serial
import os
import time
from datetime import datetime
import logging
import sys
import syslog


print "setting up"
#ser = serial.Serial("/dev/ttyUSB1", baudrate=115200, timeout=3.0)
ser = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)

logging.basicConfig(filename='./log.iot_service', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.debug("******************************************")

def sendCommand(com):
    global ser
    try:
        logging.debug('sendCommand(%s)' % com)
        return_code = 'ERROR'
        tryAgain = 'yes'
        while tryAgain == 'yes':
            if ser.isOpen():
                pass
            else:
                logging.debug('Serial Port can not be opened to send Command - check cable connections')
                ser.close()
            #ser.write(com+"\r\n")
            ser.write(com)
            logging.debug('%s : Command is %s ' % (datetime.now(), com))
            time.sleep(2)
            ret = []
            while ser.inWaiting() > 0:
                msg = ser.readline().strip()
                msg = msg.replace("\r","")
                msg = msg.replace("\n","")
                if msg!="":
                    ret.append(msg)
            logging.debug('%s : Command is %s ' % (datetime.now(), com))
            return_code = ret
            logging.debug('Last element in Command Return is %s ' % return_code)
            if 'ERROR' in return_code:
                logging.debug("Error in return code")
            else: tryAgain = 'no'
        return ret
    except:
        e = sys.exc_info()[0]
        logging.debug('%s : sendCommand() ERROR!: %s ' % (datetime.now(), e))

ret = sendCommand("AT\r\n")
print "AT"
print ret
time.sleep(2)
ret = sendCommand("AT+CFUN=1,1")
print "AT"
print ret
time.sleep(30)
ret = sendCommand("AT+UPSDA=0,0\r\n")
print "AT+UPSDA=0,0"
print ret
time.sleep(2)
ret = sendCommand("AT+CEREG=1")
print "AT+CEREG=1"
print ret
time.sleep(2)
ret = sendCommand("AT+UPSD=0,0,2\r\n")
print "AT+UPSD=0,0,2"
print ret
time.sleep(2)
ret = sendCommand("AT+UPSDA=0,3\r\n")
print "AT+UPSDA=0,3"
print ret
time.sleep(2)
ret = sendCommand("AT\r\n")
print "AT"
print ret
time.sleep(2)
ret = sendCommand("AT+CGDCONT?\r\n")
print "AT+CGDCONT"
print ret
time.sleep(2)

while True:
   #ret = ser.write("AT+UHTTP=0,1,\"google.com\"\r\n")
   ret = sendCommand('AT+UHTTP=0,1,"google.com"\r\n')
   print "AT+UHTTP"
   print ret
   time.sleep(2)
   #ret = ser.write("AT+UHTTPC=0,1,\"/\",\"r\"\r\n")
   ret = ser.write('AT+UHTTPC=0,1,"/","r"\r\n')
   print "AT+UHTTPC"
   print ret
   time.sleep(2)
   #ret = ser.write("AT+URDFILE=\"r\"\r\n")
   ret = ser.write('AT+URDFILE="r"\r\n')
   print "AT+URDFILE"
   print ret
   time.sleep(2)
   ret = sendCommand("AT\r\n")
   print "AT"
   print ret
   time.sleep(600)
