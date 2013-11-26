import time, string
import serial

from struct import unpack
from binascii import unhexlify

import numpy as np
from matplotlib import pyplot as plt


# Decode an hex representation of a float to a float
#
# See:
# http://stackoverflow.com/questions/1592158/python-convert-hex-to-float/1...
# http://stackoverflow.com/questions/4315190/single-precision-big-endian-f...
def decode_float(s):
  """Other possible implementation. Don't know what's better
  #from ctypes import *
  s = s[6:8] + s[4:6] + s[2:4] + s[0:2] # reverse the byte order
  i = int(s, 16)                   # convert from hex to a Python int
  cp = pointer(c_int(i))           # make this into a c integer
  fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
  return fp.contents.value         # dereference the pointer, get the float
  """
  return unpack('<f', unhexlify(s))[0]
  


# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/tty.usbmodemfd121',    # change this to your port id (see the bottom right of the arduino window)
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

#print(ser.open())
#print (ser.isOpen())

plt.ion() # set plot to animated

ydata = [0] * 50

ax1=plt.axes()  
 
# make plot
line, = plt.plot(ydata)
plt.ylim([10,40]) # set the y-range to 10 to 40

time.sleep(1)
ser.flushInput(); # clean input buffer

while 1 :
  value = ser.readline()
  if string.index(value, "f:") == 0:
    #print value[2:10]
    # print decode_float(value[2:10])
    # print ""
    data = decode_float(value[2:10])
    ymin = float(min(ydata))-0.05
    ymax = float(max(ydata))+0.05
    plt.ylim([ymin,ymax])
    ydata.append(data)
    del ydata[0]
    line.set_xdata(np.arange(len(ydata)))
    line.set_ydata(ydata)  # update the data
    plt.draw() # update the plot
















