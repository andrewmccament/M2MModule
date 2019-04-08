def sendCommand(com):
    global ser
    try:
        logging.debug('sendCommand(%s)' % com)
        return_code = 'ERROR'
        tryAgain = 'yes':
            while tryAgain == 'yes':
                if ser.isOpen():
                    pass
                else:
                    logging.debug('Serial Port can not be opened to send Command - check cable connections')
                    ser.close()
                ser.write(com+"\r\n")
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

