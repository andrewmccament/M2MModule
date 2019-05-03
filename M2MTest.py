#!/usr/bin/python
import M2MModule
ser = M2MModule.init()
M2MModule.reboot(ser)
M2MModule.connect(ser)
M2MModule.get(ser, "https://www.yahoo.com/")
M2MModule.firmware(ser)
M2MModule.post(ser, "postman-echo.com/post", "This is expected to be sent back as part of response body.")
