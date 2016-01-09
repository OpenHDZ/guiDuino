# -*- coding: cp1252 -*-
# Galvanomètre développé pour la librairie Tkinter
# Ecrit par Areour mohamed Cherif
# date : 24/06/2013

from Tkinter import *
from math import *
import time
from random import randrange

class Galva(Canvas):
    def __init__(self,parent):
        global valeur,root,aiguille,txt
        root=parent
        valeur=0.
        b=0
        a=0

        Canvas.__init__(self)
        #Dessin du Galva
        self.create_rectangle(0,0,200,200,fill="white",outline="white")
        self.create_rectangle(20,10,180,150,width=2,fill="white")
        self.create_rectangle(20,120,180,150,width=2,fill="grey")
        self.create_oval(25,25,175,175,width=2)
        self.create_rectangle(22,60,178,118,fill="white",outline="white")
        self.create_rectangle(22,121,178,148,fill="grey",outline="grey")
        self.create_rectangle(10,151,190,200,fill="white",outline="white")
        self.create_oval(90,125,110,145, width=2,fill="white")
        self.create_line(108,127,92,143,width=5)
        self.create_oval(95,100,105,110,fill="red",outline="red")
        a=(3-(0/50.))*(pi/4)
        x=100+90*cos(a)
        y=105-90*sin(a)
        aiguille=self.create_line(100,105,x,y,width=1,fill="red")
        txt=self.create_text(100,60, text="0",font=("courier",18,"bold"))
            
        parent.update()

    def SetValue(self,consigne):
        global valeur,root,aiguille,txt
        parent=root
        
        while (int(valeur*100+.5)!=int(consigne*100+.5)):
            if (valeur<consigne):
                valeur=valeur+(float(consigne-valeur)/50)
                float (valeur)
                a=(3-(valeur/50.))*(pi/4)
                x=100+90*cos(a)
                y=105-90*sin(a)
                self.delete(aiguille)
                self.delete(txt)
                aiguille=self.create_line(100,105,x,y,width=1,fill="red")
                txt=self.create_text(100,60, text=int(valeur),font=("courier",18,"bold") )
                parent.update()
                time.sleep(0.00002)  #Définie l'inertie de l'aiguille (Timer)
                

            elif(valeur>consigne):
                valeur=valeur+(float(consigne-valeur)/50)
                float (valeur)
                a=(3-(valeur/50.))*(pi/4)
                x=100+90*cos(a)
                y=105-90*sin(a)
                self.delete(aiguille)
                self.delete(txt)
                aiguille=self.create_line(100,105,x,y,width=1,fill="red")
                txt=self.create_text(100,60, text=int(valeur),font=("courier",18,"bold") )
                parent.update()
                time.sleep(0.00002)  #Définie l'inertie de l'aiguille (Timer)
                

            else:
                float (valeur)
                a=(3-(valeur/50.))*(pi/4)
                x=100+90*cos(a)
                y=105-90*sin(a)
                self.delete(aiguille)
                self.delete(txt)
                aiguille=self.create_line(100,105,x,y,width=1,fill="red")
                txt=can.create_text(100,60, text=int(valeur),font=("courier",18,"bold") )
                parent.update()
                time.sleep(0.00002)       #Définie l'inertie de l'aiguille (Timer)
                

def val():
    for i in range(1,100):
        gal.SetValue(randrange(100))
        

if __name__=="__main__":
    app=Tk()
    gal=Galva(app)
    gal.pack()
    val()
    
    app.mainloop()
    
