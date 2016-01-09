import Tkinter
import time
from random import randrange

class Mod_gauge(Tkinter.Canvas):
    def __init__(self, parent):
        global valeur, root, arc, text, H, W

        root = parent
        valeur = 0.
        H=260
        W=260


        Tkinter.Canvas.__init__(self, bg="#3300FF", height=H, width=W)
        # Dessin de la gauge
        self.create_oval((H-210), (W-215), (H-50), (W-50), fill="#3300FF", outline="#3300FF")       

        arc = self.create_arc((H-240), (W-240), (H-20), (W-20), start=90, extent = valeur, fill="#3399FF",outline="#3399FF")    
        text = self.create_text(130, 130, text=int(valeur), font="Arial 40 italic", fill="#3399FF")
        
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
                arc = self.create_arc((H-240), (W-240), (H-20), (W-20), start=90, extent=-valeur, fill="#3399FF",outline="#3399FF")
                self.create_oval((H-210), (W-215), (H-50), (W-50), fill="#3300FF", outline="#3300FF")
                text = self.create_text(130, 130, text=int(txt_consigne), font="Arial 40 italic", fill="#3399FF")
                parent.update()
                #time.sleep(0.00002)    #Définie l'inertie de la gauge

            elif( int(valeur) > int(consigne*3.6)):
                valeur = valeur - 1
                txt_consigne = valeur/3.6
                self.delete(arc)
                self.delete(text)
                arc = self.create_arc((H-240), (W-240), (H-20), (W-20), start=90, extent=-valeur, fill="#3399FF",outline="#3399FF")
                self.create_oval((H-210), (W-215), (H-50), (W-50), fill="#3300FF", outline="#3300FF")
                text = self.create_text(130, 130, text=int(txt_consigne), font="Arial 40 italic", fill="#3399FF")
                parent.update()
                #time.sleep(0.00002)    #Définie l'inertie de la gauge
                
            else :
                txt_consigne = valeur/3.6
                self.delete(arc)
                self.delete(text)
                arc = self.create_arc((H-240), (W-240), (H-20), (W-20), start=90, extent=-valeur, fill="#3399FF",outline="#3399FF")
                self.create_oval((H-210), (W-215), (H-50), (W-50), fill="#3300FF", outline="#3300FF")
                text = self.create_text(130, 130, text=int(txt_consigne), font="Arial 40 italic", fill="#3399FF")
                parent.update()
                #time.sleep(0.00002)    #Définie l'inertie de la gauge

def val():
    for i in range(1,10):
        gauge.SetValue(randrange(10))

if __name__=="__main__":
    app=Tkinter.Tk()
    gauge=Mod_gauge(app)
    gauge.pack()
    val()
    
    app.mainloop()
