#!/usr/bin/python
import M2MModule
import M2MConnect
varTest = "test"
ser = M2MModule.init()
M2MModule.connect(ser)
M2MModule.get(ser, "http://www.google.com")
