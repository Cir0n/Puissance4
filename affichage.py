from tkinter import *

#configurations de la fenetre puissance 4
fenetre = Tk()
fenetre.title('Puissance 4 - Menu')
fenetre.iconbitmap('image/puissance4.ico')
fenetre.config(bg="#7092be")
fenetre.geometry('640x480')
cadre = Frame(fenetre)
titre = Label(cadre, text='Menu',bg='#7092be',fg='black', font=('Arial'))
cadre.pack()
quitButton = Button(fenetre, text = "Quitter", command = exit, width= 10, height= 2)
quitButton.pack()
fenetre.mainloop()
