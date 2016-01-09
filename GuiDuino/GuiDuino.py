# -*- coding: cp1252 -*-
# GuiDuino interface graphique pour Arduino
# Version : 0.01 
# Ecrit par Areour mohamed Cherif
# date : 27/04/2014

from Tkinter import *
import serial
import galva

ser=serial.Serial('/dev/ttyACM0',9600)
print ser

app=Tk()
app.title('GuiDuino v0.01')
gal=galva.Galva(app)
gal.pack()

def val():
    
    x = ser.readline()
    x.strip()
    gal.SetValue(int(x))
    app.after(10, val)

app.after(50, val)

app.mainloop()

