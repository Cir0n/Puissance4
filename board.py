from tkinter import *
import numpy as np

fenetre = Tk()
nb = 0


def increment():
    global nb
    nb += 1
    bouton.config(text=str(nb))


label = Label(fenetre, text="Tkinter test")
label.pack()

fenetre.minsize(300, 200)

bouton = Button(fenetre, text=str(nb), command=increment)
bouton.pack()
fenetre.mainloop()
