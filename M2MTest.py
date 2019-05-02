#!/usr/bin/python
import M2MModule
varTest = "test"
ser = M2MModule.init()
M2MModule.reboot(ser)
M2MModule.connect(ser)
M2MModule.get(ser, "http://www.yahoo.com")
M2MModule.post(ser, "https://postman-echo.com/post", "This is expected to be sent back as part of response body.")
print "test is finished!"
