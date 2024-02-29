from tkinter import *
import tkinter.font as tkFont

def buttion_click(btn, row, col):
    print(row,col)
    btn.config()

# Configurations de la fenetre puissance 4
window = Tk()
window.title("Puissance 4")
window.iconbitmap("image/puissance4.ico")
window.geometry("1080x720")
window.minsize(720, 480)
window.config(background='#7092BE')

def clear():
    """
    efface tous les slaves de la window
    """
    list = window.grid_slaves()
    for l in list:
        l.destroy()

    list = window.slaves()
    for l in list:
        l.destroy()


def affiche_menu():
    clear()

    # Création du titre
    title_label = Label(window, text="Menu", font=("Courier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid(row=1, column =3, sticky=NS)

    font_style = tkFont.Font(family='Courier', size=20)

    local_button = Button(window, text="Jouer en local", command=affiche_partie_locale, font=font_style, width=20, pady=20, bd=0, highlightthickness=0)
    local_button.grid(row=2, column=3,sticky=NS, padx=360)

    quit_button = Button(window, text="Quitter", command=window.destroy, pady=20, fg='black', bd=0, highlightthickness=0, width=20, font=font_style)
    quit_button.grid(row=4, column=3,sticky=NS, pady=20)

def affiche_partie_locale():
    clear()
    title_label = Label(window, text="Partie en local", font=("Courrier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid()

    font_style = tkFont.Font(family='Courier', size=20)

    retour_button = Button(window, text="Retour au menu", command=affiche_menu, pady=20, fg='black', bd=0,highlightthickness=0, width=20, font=font_style)
    retour_button.grid(row=2, column=1)


def affiche_partie_deux():
    clear()
    title_label = Label(window, text="Partie à 2", font=("Courrier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid()


def affiche_partie_ordi():
    clear()
    title_label = Label(window, text="Niveaux de l'ordinateur", font=("Courrier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid()


def affiche_partie_en_ligne():
    clear()
    title_label = Label(window, text="Jouer en ligne", font=("Courrier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid()


def affiche_creer_en_ligne():
    clear()
    title_label = Label(window, text="En attente d'un joueur...", font=("Courrier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid()


def affiche_rejoindre_partie_en_ligne():
    clear()
    title_label = Label(window, text="Rejoindre une partie", font=("Courrier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid()




affiche_menu()
# Afficher la fenêtre
window.mainloop()
