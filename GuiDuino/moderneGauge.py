# -*- coding: cp1252 -*-

"""
Gauge développé pour la librairie Tkinter
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

import Tkinter
import time
from random import randrange

class Mod_gauge(Tkinter.Canvas):
    def __init__(self, parent, titre = "Gauge"):
        global valeur, root, arc, text, H, W, coord1, coord2

        self.titre = titre
        root = parent
        valeur = 0.
        H=290
        W=260
        coord1 = (H-240), (W-215), (H-80), (W-50)
        coord2 = (H-270), (W-240), (H-50), (W-20)

        Tkinter.Canvas.__init__(self, bg="#FF2E2E", height=H, width=W)

        # Dessin de la gauge
        self.create_oval(coord1, fill="#FF2E2E", outline="#FF8B8B")
        #self.create_oval(coord1, outline="#3399FF")

        arc = self.create_arc(coord2, start=90, extent = valeur, fill="#FF8B8B",outline="#FF8B8B")
        self.create_oval(coord2, outline="#FF8B8B")
        text = self.create_text(130, 130, text=int(valeur), font="Arial 40 italic", fill="#FF8B8B")
        legende = self.create_text(130, 260, text= self.titre, font="Arial 20 ", fill="#FF8B8B")
        
        parent.update()

    def SetValue(self, consigne):
        global valeur, root, arc, text
        parent = root

        while (int(valeur) != int(consigne*3.6)):

            if (int(valeur) < int(consigne*3.6)):
                valeur = valeur + 1
                txt_consigne = valeur/3.6
                self.delete(arc)
                self.delete(text)
                arc = self.create_arc(coord2, start=90, extent=-valeur, fill="#FF8B8B")
                self.create_oval(coord2, outline="#FF8B8B")
                self.create_oval(coord1, fill="#FF2E2E", outline="#FF8B8B")
                self.create_oval(coord1, outline="#FF8B8B")
                text = self.create_text(130, 130, text=int(txt_consigne), font="Arial 40 italic", fill="#FF8B8B")
                parent.update()
                #time.sleep(0.00002)    #Définie l'inertie de la gauge

            elif( int(valeur) > int(consigne*3.6)):
                valeur = valeur - 1
                txt_consigne = valeur/3.6
                self.delete(arc)
                self.delete(text)

                arc = self.create_arc(coord2, start=90, extent=-valeur, fill="#FF8B8B")
                self.create_oval(coord2, outline="#FF8B8B")
                self.create_oval(coord1, fill="#FF2E2E", outline="#FF8B8B")
                self.create_oval(coord1, outline="#FF8B8B")
                text = self.create_text(130, 130, text=int(txt_consigne), font="Arial 40 italic", fill="#FF8B8B")
                parent.update()
                #time.sleep(0.00002)    #Définie l'inertie de la gauge
                
            else :
                txt_consigne = valeur/3.6
                self.delete(arc)
                self.delete(text)
                arc = self.create_arc(coord2, start=90, extent=-valeur, fill="#FF8B8B")
                self.create_oval(coord2, outline="#FF8B8B")
                self.create_oval(coord1, fill="#FF2E2E", outline="#FF8B8B")
                self.create_oval(coord1, outline="#FF8B8B")
                text = self.create_text(130, 130, text=int(txt_consigne), font="Arial 40 italic", fill="#FF8B8B")
                parent.update()
                #time.sleep(0.00002)    #Définie l'inertie de la gauge

def val():
    for i in range(1,10):
        gauge.SetValue(randrange(100))

if __name__=="__main__":
    app=Tkinter.Tk()
    gauge=Mod_gauge(app)
    gauge.pack()
    val()
    
    app.mainloop()
