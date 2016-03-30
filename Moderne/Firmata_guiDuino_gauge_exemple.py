# -*- coding: cp1252 -*-
"""
Exemple d'utilisation de la class Mod_gauge développé pour la librairie Tkinter
Ecrit par Areour mohamed Cherif
Date : 10/01/2016
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
import pyfirmata 
import moderneGauge

port = '/dev/ttyACM1'
board = pyfirmata.Arduino(port)

analogPin = board.get_pin('a:0:i')

#Use iterator thread to	avoid	buffer	overflow
it = pyfirmata.util.Iterator(board)
it.start()

app=Tk()
app.title('GuiDuino v0.03')
gauge=moderneGauge.Mod_gauge(app, titre = "Humidity")
gauge.pack()

def val():
    
    x = analogPin.read()
    print type(x)
    y = (x*50.)
    print y
    gauge.SetValue(int(y))
    app.after(10, val)

app.after(50, val)

app.mainloop()
board.exit()

