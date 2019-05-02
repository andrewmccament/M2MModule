#!/usr/bin/python
import serial
import os
import time
from datetime import datetime
import logging
import sys
import syslog

global ser

def init():
    print "setting up"
    ser = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
    
    logging.basicConfig(filename='./log.iot_service', level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.debug("******************************************")
    return ser

def reboot(ser):
    ret = sendCommand("AT\r\n", ser)
    print ret
    time.sleep(2)
    ret = sendCommand("AT+CFUN=1,1", ser)
    print ret
    time.sleep(30)
    print "LARA-R2 modem rebooted"
    
def connect(ser):
    ret = sendCommand("AT+CEREG=1", ser)
    print ret
    time.sleep(2)
    ret = sendCommand("AT+UPSD=0,0,2\r\n", ser)
    print ret
    time.sleep(2)
    ret = sendCommand("AT+UPSD=0,1,\"VZWINTERNET\"\r\n", ser)
    time.sleep(2)
    ret = sendCommand("AT+UPSDA=0,3\r\n", ser)
    print ret
    time.sleep(2)
    return True

def get(ser, address):
    ret = sendCommand("AT+CGDCONT?\r\n", ser)
    print "AT+CGDCONT"
    print ret
    time.sleep(2)
    
    while True:
        ret = sendCommand("AT+UHTTP=0,1,\"" + address + "\"\r\n", ser)
        print ret
        time.sleep(2)
        print 'Attempting ' + 'AT+UHTTPC=0,1,"/","r"\r\n'
        ret = ser.write('AT+UHTTPC=0,1,"/","r"\r\n')
        print ret
        time.sleep(2)
        print 'Attempting ' + 'AT+URDFILE="r"\r\n'
        ret = ser.write('AT+URDFILE="r"\r\n')
        print ret
        time.sleep(2)
        print
        print ret
        time.sleep(6)
        return True

def post(ser, address, data):
    while True:
        ret = sendCommand('AT+UHTTP=0,1,"' + address + '"\r\n', ser)
        print ret
        time.sleep(2)
        print 'Attempting ' + 'AT+UHTTPC=0,5,"/","r","' + data + '",0\r\n'
        ret = ser.write('AT+UHTTPC=0,5,"/","r","' + data + '",0\r\n')
        print ret
        time.sleep(2)
        print 'Attempting ' + 'AT+URDFILE="r"\r\n'
        ret = ser.write('AT+URDFILE="r"\r\n')
        print ret
        time.sleep(2)
        ret = sendCommand("AT\r\n", ser)
        print ret
        time.sleep(6)
        return True

def sendCommand(command, ser):
    try:
        logging.debug('sendCommand(%s)' % command)
        return_code = 'ERROR'
        tryAgain = 'yes'
        loopCount = 0;
        while tryAgain == 'yes':
            loopCount+=1
            if (loopCount > 25):
                print "Error: operation " + command + " timed out with errors"
                return ret;
            print command
            if not ser.isOpen():
                logging.debug('Serial Port can not be opened to send Command - check cable connections')
                ser.close()
            ser.write(command)
            logging.debug('%s : Command is %s ' % (datetime.now(), command))
            time.sleep(2)
            ret = []
            while ser.inWaiting() > 0:
                msg = ser.readline().strip()
                msg = msg.replace("\r","")
                msg = msg.replace("\n","")
                if msg!="":
                    ret.append(msg)
            logging.debug('%s : Command is %s ' % (datetime.now(), command))
            return_code = ret
            logging.debug('Last element in Command Return is %s ' % return_code)
            if 'ERROR' in return_code:
                logging.debug("Error in return code")
            else: tryAgain = 'no'
        return ret
    except:
        e = sys.exc_info()[0]
        logging.debug('%s : sendCommand() ERROR!: %s ' % (datetime.now(), e))
