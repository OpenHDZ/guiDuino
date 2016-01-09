# -*- coding: cp1252 -*-
# GuiDuino interface graphique pour Arduino
# Version : 0.01 
# Ecrit par Areour mohamed Cherif
# date : 27/04/2014

import serial
import time
from pylab import *

ser=serial.Serial('USB',9600)
print ser

def val():
    x = ser.readline()
    x.strip()
    return float(x)

ion()

x = linespace(0, 5, 1000)
y = float(ser.readline())
line, =plot(x,y)

while 1:
    y = val()
    line.set_ydata(y)
    draw()
    
    time.sleep(0.00002)

ioff()