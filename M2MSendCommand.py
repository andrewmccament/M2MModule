#!/usr/bin/python
import serial
import os
import time
from datetime import datetime
import logging
import sys
import syslog

def sendCommand(command, ser):
    try:
        logging.debug('sendCommand(%s)' % command)
        return_code = 'ERROR'
        tryAgain = 'yes'
        while tryAgain == 'yes':
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
