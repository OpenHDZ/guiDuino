# -*- coding: cp1252 -*-

"""
Barre de niveau developper pour la librairie Tkinter
Ecrit par Areour mohamed Cherif
Date : 18/01/2016
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
from time import sleep
from random import randrange

class Mod_prog(Tkinter.Canvas):
    def __init__(self, parent, titre = "Niveau", height=160, width=600):
        global valeur, root, bar, grad, text, H, W, coord1, coord2

        self.titre = titre
        root = parent
        valeur = 30
        H=height
        W=width
        coord1 = 30, 40, (W-30), (H-40) 
        coord2 = 30, 40, 31, (H-40)

        Tkinter.Canvas.__init__(self, bg="red", height=H, width=W)

        # Dessin de la barre 
        self.create_rectangle(coord1, outline="#FF8B8B")

        bar = self.create_rectangle(coord2, fill="#FF8B8B",outline="#FF8B8B")
        grad = self.create_line(31,35, 31, 40, fill = "#FF8B8B") 
        text = self.create_text(31, 20, text=int(valeur), font="Arial 20 italic", fill="#FF8B8B")
        legende = self.create_text((W/2),(H-25) , text= self.titre, font="Arial 20 italic", fill="#FF8B8B")
        
        parent.update()

    def SetValue(self, consigne):
        global valeur, root, bar, text, grad, H, W 
        parent = root
        bar_consigne = consigne*(W-30)/100 # valeur de la consigne en pixel
                
        while (int(valeur) != bar_consigne):

            if (int(valeur) < bar_consigne):
                valeur = valeur + 1
                 
                txt_consigne = (valeur*100)/(W-30)

                self.delete(bar)
                self.delete(grad)
                self.delete(text)

                bar = self.create_rectangle(30, 40, valeur, H-40, fill="#FF8B8B",outline="#FF8B8B")
                grad = self.create_line(valeur,35, valeur, 40, fill = "#FF8B8B")
                text = self.create_text(valeur,20, text=txt_consigne, font="Arial 20 italic", fill="#FF8B8B")

                parent.update()
                sleep(0.02)
                

            elif(int(valeur) > bar_consigne):

                valeur = valeur - 1
                txt_consigne = (valeur*100)/(W-30)

                self.delete(bar)
                self.delete(grad)
                self.delete(text)

                bar = self.create_rectangle(30, 40, valeur, H-40, fill="#FF8B8B",outline="#FF8B8B")
                grad = self.create_line(valeur,35, valeur, 40, fill = "#FF8B8B")
                text = self.create_text(valeur,20, text=int(txt_consigne), font="Arial 20 italic", fill="#FF8B8B")

                parent.update()
                sleep(0.02)
                
                
            else :
                txt_consigne = (valeur*100)/(W-30)

                self.delete(bar)
                self.delete(grad)                
                self.delete(text)

                bar = self.create_rectangle(30, 40, valeur, H-40, fill="#FF8B8B",outline="#FF8B8B")
                grad = self.create_line(valeur,35, valeur, 40, fill = "#FF8B8B")
                text = self.create_text(valeur,20, text=int(txt_consigne), font="Arial 20 italic", fill="#FF8B8B")
                parent.update()
                sleep(0.02)

def val():
    for i in range(1,10):
        barre.SetValue(100)#randrange(100))

if __name__=="__main__":
    app=Tkinter.Tk()
    barre=Mod_prog(app, titre = "Progression",height=160, width=800)
    barre.pack()
    val()
    
    app.mainloop()
