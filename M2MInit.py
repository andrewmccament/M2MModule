#!/usr/bin/python
import serial
import os
import time
from datetime import datetime
import logging
import sys
import syslog

def init():
    print "setting up"
    ser = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)

    logging.basicConfig(filename='./log.iot_service', level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.debug("******************************************")
    return ser
