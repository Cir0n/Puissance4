import time
from tkinter import *
import tkinter.font as tkFont
from board import *
from client import *
from serveur import *
import threading


def colorie_tableau(tableau):
    """
    paramètres : tableau numpy de dimensions 6,7

    prend le tableau actuel et change le png des boutons par rapport aux joueurs
    si case de la position du bouton 0,4 = 1 alors le png change en rouge
    """
    image_rouge = PhotoImage(file="image/case_rouge.png")
    image_jaune = PhotoImage(file="image/case_jaune.png")
    for i in range(6):
        for j in range(7):
            button = buttons[i][j]
            if tableau[i][j] == 1:
                button.configure(image=image_rouge, width=100, height=102, bd=0, highlightthickness=0)
                button.image = image_rouge
            elif tableau[i][j] == 2:
                button.configure(image=image_jaune, width=100, height=102, bd=0, highlightthickness=0)
                button.image = image_jaune
        window.update()


def stop_buttons():
    for i in range(6):
        for j in range(7):
            button = buttons[i][j]
            button.configure(command=0)
    window.update()


def activate_buttons(lvl):
    for i in range(6):
        for j in range(7):
            button = buttons[i][j]
            if lvl == 0:
                button.configure(command=lambda row=i, col=j: on_button_click(row, col))
            elif lvl == 1:
                button.configure(command=lambda row=i, col=j: on_button_click_ordi_facile(row, col))
            elif lvl == 2:
                button.configure(command=lambda row=i, col=j: on_button_click_ordi_moyen(row, col))
            elif lvl == 3:
                button.configure(command=lambda row=i, col=j: on_button_click_ordi_difficile(row, col))
            elif lvl == 4:
                button.configure(command=lambda row=i, col=j: on_button_click_online_serveur(row, col))
            elif lvl == 5:
                button.configure(command=lambda row=i, col=j: on_button_click_online_client(row, col))
            window.update()

def att_adversaire_joue_client():
    global tableau
    while True:
        coup_adversaire = get_data_client()
        if coup_adversaire != None:
            coup_adversaire = int(coup_adversaire.decode())
            activate_buttons(5)
            tmp = np.array(tableau)
            tmp, gagnant = jouer(tmp, coup_adversaire)
            if not np.array_equal(tmp, tableau):
                tableau = tmp
                colorie_tableau(tableau)
                designe_joueur()
                if gagnant is not None:
                    stop_buttons()
                    afficher_gagnant(gagnant)
                    time.sleep(1.5)
                    break
                break
            break
    return

def att_adversaire_joue_serveur():
    global tableau
    while True:
        coup_adversaire = get_data_serveur()
        if coup_adversaire != None:
            coup_adversaire = int(coup_adversaire.decode())
            activate_buttons(4)
            tmp = np.array(tableau)
            tmp, gagnant = jouer(tmp, coup_adversaire)
            if not np.array_equal(tmp, tableau):
                tableau = tmp
                colorie_tableau(tableau)
                designe_joueur()
                if gagnant is not None:
                    stop_buttons()
                    afficher_gagnant(gagnant)
                    time.sleep(1.5)
                    break
                break
            break
    return


def on_button_click(row, col):
    """
    fonction du bouton qui renvoie la position du bouton
    """
    global tableau
    print(f"Bouton cliqué en {row} {col}")
    tmp = np.array(tableau)
    tmp, gagnant = jouer(tmp, col)
    if not np.array_equal(tmp, tableau):
        tableau = tmp
        print(tableau)
        colorie_tableau(tableau)
        designe_joueur()
        if gagnant is not None:
            stop_buttons()
            time.sleep(1.5)
            afficher_gagnant(gagnant)


def on_button_click_online_serveur(row, col):
    """
    fonction du bouton qui renvoie la position du bouton
    """
    global tableau
    print(f"Bouton cliqué en {row} {col}")
    tmp = np.array(tableau)
    tmp, gagnant = jouer(tmp, col)
    if not np.array_equal(tmp, tableau):
        tableau = tmp
        print(tableau)
        colorie_tableau(tableau)
        designe_joueur()
        envoie_pos_joue_serveur(col)  # envoie à l'adversaire la pos jouée
        stop_buttons()
        if gagnant is not None:
            stop_buttons()
            time.sleep(1.5)
            afficher_gagnant(gagnant)
        thread_attente_adversaire = threading.Thread(target=att_adversaire_joue_serveur)
        thread_attente_adversaire.start()


def on_button_click_online_client(row, col):
    """
    fonction du bouton qui renvoie la position du bouton
    """
    global tableau
    print(f"Bouton cliqué en {row} {col}")
    tmp = np.array(tableau)
    tmp, gagnant = jouer(tmp, col)
    if not np.array_equal(tmp, tableau):
        tableau = tmp
        print(tableau)
        colorie_tableau(tableau)
        designe_joueur()
        envoie_pos_joue_client(col)  # envoie à l'adversaire la pos jouée
        stop_buttons()
        if gagnant is not None:
            stop_buttons()
            time.sleep(1.5)
            afficher_gagnant(gagnant)
        thread_attente_adversaire = threading.Thread(target=att_adversaire_joue_client)
        thread_attente_adversaire.start()


def on_button_click_ordi_facile(row, col):
    """
    fonction du bouton qui renvoie la position du bouton
    """
    global tableau
    print(f"Bouton cliqué en {row} {col}")
    tmp = np.array(tableau)
    tmp, gagnant = jouer(tmp, col)
    designe_joueur()
    if not np.array_equal(tmp, tableau):
        tableau = tmp
        print(tableau)
        colorie_tableau(tableau)
        if gagnant is not None:
            stop_buttons()
            time.sleep(1.5)
            afficher_gagnant(gagnant)
        else:
            tmp, gagnant = ordi_facile_joue(tableau)
            designe_joueur()
            if np.array_equal(tmp, tableau):
                tableau = tmp
            colorie_tableau(tableau)
            if gagnant is not None:
                stop_buttons()
                time.sleep(1.5)
                afficher_gagnant(gagnant)


def on_button_click_ordi_moyen(row, col):
    global tableau
    print(f"Bouton cliqué en {row} {col}")
    tmp = np.array(tableau)
    tmp, gagnant = jouer(tmp, col)
    if not np.array_equal(tmp, tableau):
        tableau = tmp
        print(tableau)
        designe_joueur()
        colorie_tableau(tableau)
        if gagnant is not None:
            stop_buttons()
            time.sleep(1.5)
            afficher_gagnant(gagnant)
        else:
            tmp, gagnant = ordi_moyen_joue(tableau)
            designe_joueur()
            if np.array_equal(tmp, tableau):
                tableau = tmp
            colorie_tableau(tableau)
            if gagnant is not None:
                stop_buttons()
                time.sleep(1.5)
                afficher_gagnant(gagnant)


def on_button_click_ordi_difficile(row, col):
    global tableau
    print(f"Bouton cliqué en {row} {col}")
    tmp = np.array(tableau)
    tmp, gagnant = jouer(tmp, col)
    if not np.array_equal(tmp, tableau):
        tableau = tmp
        print(tableau)
        designe_joueur()
        colorie_tableau(tableau)
        if gagnant is not None:
            stop_buttons()
            time.sleep(1.5)
            afficher_gagnant(gagnant)
        else:
            tmp, gagnant = ordi_difficile_joue(tableau)
            designe_joueur()
            if np.array_equal(tmp, tableau):
                tableau = tmp
            colorie_tableau(tableau)
            if gagnant is not None:
                stop_buttons()
                time.sleep(1.5)
                afficher_gagnant(gagnant)


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

    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)


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

    partie_joueurs_button = Button(window, text="Jouer à 2", command=lambda lvl=0: jeu(lvl), font=font_style,
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
    # Création du titre
    title_label = Label(window, text="Niveaux de l'ordinateur", font=("Courier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid(row=1, column=1, columnspan=3, sticky=EW)

    font_style = tkFont.Font(family='Courier', size=20)

    facile_button = Button(window, text="Facile", command=lambda lvl=1: jeu(lvl), font=font_style,
                           width=20, pady=20, bd=0, highlightthickness=0)
    facile_button.grid(row=2, column=2, columnspan=1, sticky=EW, pady=15)

    moyen_button = Button(window, text="Moyen", command=lambda lvl=2: jeu(lvl),
                          font=font_style, width=20, pady=20, bd=0, highlightthickness=0)
    moyen_button.grid(row=3, column=2, columnspan=1, sticky=EW, pady=15)

    difficile_button = Button(window, text="Difficile", command=lambda lvl=3: jeu(lvl), font=font_style,
                              width=20, pady=20, bd=0, highlightthickness=0)
    difficile_button.grid(row=4, column=2, columnspan=1, sticky=EW, pady=15)

    retour_button = Button(window, text="Retour", command=affiche_partie_locale, pady=20, fg='black', bd=0,
                           highlightthickness=0, font=font_style)
    retour_button.grid(row=5, column=2, columnspan=1, sticky=EW, pady=35, padx=40)


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
    thread_creer_partie = threading.Thread(target=creer_serveur)
    thread_lance_jeu = threading.Thread(target=jeu, args=(4,))
    thread_lance_jeu.start()
    thread_creer_partie.start()

def affiche_rejoindre_partie_en_ligne():
    clear()
    title_label = Label(window, text="Rejoindre une partie", font=("Courrier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid(row=0, column=1, columnspan=3, sticky=EW)

    text_label = Label(window, text="IP du serveur :", font=("Courrier", 30), bg='#7092BE', fg='white', pady=30)
    text_label.grid(row=2, column=1)

    entree = StringVar()
    entry = Entry(window, font=("Courrier", 48), bg='#7092BE', fg='white', textvariable=entree)
    entry.grid(row=2, column=2, columnspan=1, sticky=EW, pady=15)
    entry.focus()

    connect_button = Button(window, text="Connect", bg='white', fg='black',
                            command=lambda ip=entree: rejoindre_partie(ip))
    connect_button.grid(row=3, column=2, columnspan=2, sticky=S)


def rejoindre_partie(ip):
    thread_rejoindre_partie = threading.Thread(target=connect, args=(ip,))
    thread_lance_jeu = threading.Thread(target=jeu, args=(5,))
    thread_rejoindre_partie.start()
    thread_lance_jeu.start()

def jeu(lvl):
    clear()
    frame = Frame(window, bg='#7092BE')
    image_vide = PhotoImage(file="image/case_vide.png")
    for i in range(6):
        for j in range(7):
            button = Button(frame, image=image_vide, width=100, height=102, bg="white",
                            command=lambda row=i, col=j: on_button_click(row, col), bd=0, highlightthickness=0)
            button.image = image_vide
            button.grid(row=i, column=j)
            buttons[i][j] = button
    frame.pack(side=BOTTOM)
    designe_joueur()
    activate_buttons(lvl)
    if lvl == 5:
        stop_buttons()
        thread_attente_adversaire = threading.Thread(target=att_adversaire_joue_client)
        thread_attente_adversaire.start()
    window.grid_columnconfigure(1, weight=0)
    window.grid_columnconfigure(2, weight=0)
    window.grid_columnconfigure(3, weight=0)


def afficher_gagnant(joueur):
    colorie_tableau(tableau)
    clear()
    font_style = tkFont.Font(family='Courier', size=20)
    text = f"Joueur {joueur} a gagné"
    if joueur == "égalité":
        text = "égalité"
    title_label = Label(window, text=text, font=("Courier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid(column=2, row=0)
    button = Button(window, text="Menu", command=affiche_menu, pady=20, bg='white', highlightthickness=0,
                    font=font_style)
    button.grid(row=4, column=2, sticky=EW, pady=35, padx=40)
    recommencer_partie()


def recommencer_partie():
    global tableau
    global tour
    tableau = np.zeros([6, 7])
    tour = 0
    reinitialiser_joueur()


def designe_joueur():
    # Afficher tour du joueur
    for l, i in enumerate(window.slaves()):
        if l == 1:
            i.destroy()
            break
    joueur = get_joueur()
    title_frame = Frame(window, bg='#7092BE')
    text = f"tour du Joueur : {joueur}"
    designe_tour = Label(title_frame, text=text, font=("Courrier", 30), bg='#7092BE', fg='white', pady=30)
    designe_tour.pack()
    title_frame.pack(side=TOP)


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
