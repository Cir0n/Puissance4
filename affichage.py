from tkinter import *
import tkinter.font as tkFont
from board import *


def on_button_click(col):
    print(f"Button clicked at column {col}")
    print(buttons[0][col])



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
    title_label.grid(row=1, column=1, columnspan=3, sticky=EW)

    font_style = tkFont.Font(family='Courier', size=20)

    local_button = Button(window, text="Jouer en local", command=affiche_partie_locale, font=font_style,
                          width=20, pady=20, bd=0, highlightthickness=0)
    local_button.grid(row=2, column=2, columnspan=1, sticky=EW, pady=15)

    online_button = Button(window, text="Jouer en ligne", command=affiche_partie_en_ligne,
                           font=font_style, width=20, pady=20, bd=0, highlightthickness=0)
    online_button.grid(row=3, column=2, columnspan=1, sticky=EW, pady=15)

    rule_button = Button(window, text="Voir les règles", command=affiche_partie_locale, font=font_style,
                         width=20, pady=20, bd=0, highlightthickness=0)
    rule_button.grid(row=4, column=2, columnspan=1, sticky=EW, pady=15)

    quit_button = Button(window, text="Quitter", command=window.destroy, pady=20, fg='black', bd=0,
                         highlightthickness=0, font=font_style)
    quit_button.grid(row=5, column=2, columnspan=1, sticky=EW, pady=35, padx=40)


def affiche_partie_locale():
    clear()
    # Création du titre
    title_label = Label(window, text="Partie locale", font=("Courier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid(row=1, column=1, columnspan=3, sticky=EW)

    font_style = tkFont.Font(family='Courier', size=20)

    partie_joueurs_button = Button(window, text="Jouer à 2", command=jeu_local, font=font_style,
                                   width=20, pady=20,
                                   bd=0, highlightthickness=0)
    partie_joueurs_button.grid(row=2, column=2, columnspan=1, sticky=EW, pady=15)

    ordi_button = Button(window, text="Jouer contre l'ordinateur", command=affiche_partie_ordi,
                         font=font_style, width=20, pady=20, bd=0, highlightthickness=0)
    ordi_button.grid(row=3, column=2, columnspan=1, sticky=EW, pady=15)

    quit_button = Button(window, text="Retour au menu", command=affiche_menu, pady=20, fg='black', bd=0,
                         highlightthickness=0, font=font_style)
    quit_button.grid(row=4, column=2, columnspan=1, sticky=EW, pady=35, padx=40)


def affiche_partie_ordi():
    clear()
    title_label = Label(window, text="Niveaux de l'ordinateur", font=("Courrier", 48), bg='#7092BE', fg='white',
                        pady=30)
    title_label.grid()


def affiche_partie_en_ligne():
    clear()
    # Création du titre
    title_label = Label(window, text="Partie en ligne", font=("Courier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid(row=1, column=1, columnspan=3, sticky=EW)

    font_style = tkFont.Font(family='Courier', size=20)

    creer_partie_button = Button(window, text="Créer une partie", command=affiche_creer_en_ligne,
                                 font=font_style, width=20, pady=20, bd=0, highlightthickness=0)
    creer_partie_button.grid(row=2, column=2, columnspan=1, sticky=EW, pady=15)

    rejoindre_button = Button(window, text="Rejoindre une partie",
                              command=affiche_rejoindre_partie_en_ligne, font=font_style, width=20,
                              pady=20, bd=0, highlightthickness=0)
    rejoindre_button.grid(row=3, column=2, columnspan=1, sticky=EW, pady=15)

    quit_button = Button(window, text="Retour au menu", command=affiche_menu, pady=20, fg='black', bd=0,
                         highlightthickness=0, font=font_style)
    quit_button.grid(row=4, column=2, columnspan=1, sticky=EW, pady=35, padx=40)


def affiche_creer_en_ligne():
    clear()
    title_label = Label(window, text="En attente d'un joueur...", font=("Courrier", 48), bg='#7092BE', fg='white',
                        pady=30)
    title_label.grid()


def affiche_rejoindre_partie_en_ligne():
    clear()
    title_label = Label(window, text="Rejoindre une partie", font=("Courrier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid()


def creer_rond(x, y, r, window):  # coordonnées, rayon
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    rond = window.create_oval(x0, y0, x1, y1)
    return rond


def grille():
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)


def jeu_local():
    clear()
    frame = Frame(window, bg='#7092BE')
    image_vide = PhotoImage(file="image/case_vide.png")
    for i in range(6):
        for j in range(7):
            button = Button(frame, image=image_vide, width=100, height=102, bg="white", command=lambda col=j: on_button_click(col), bd=0, highlightthickness=0)
            button.image = image_vide
            button.grid(row=i, column=j)
            buttons[i][j] = button
    frame.pack(side=BOTTOM)

    window.grid_columnconfigure(1, weight=0)
    window.grid_columnconfigure(2, weight=0)
    window.grid_columnconfigure(3, weight=0)


# Configurations de la fenetre puissance 4
window = Tk()
window.title("Puissance 4")
window.iconbitmap("image/puissance4.ico")
window.geometry("1080x720")
window.minsize(720, 480)
window.config(background='#7092BE')

window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

buttons = [[None for _ in range(7)] for _ in range(6)]

affiche_menu()

# Afficher la fenêtre
window.mainloop()


def jeu_ordi(window):
    print()
