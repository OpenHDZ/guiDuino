# -*- coding: cp1252 -*-

"""
Exemple d'utilisation du Galvanomètre développé pour la librairie Tkinter
Ecrit par Areour mohamed Cherif
Date : 27/04/2014
E-mail : openhardwaredz@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

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

