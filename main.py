import time
from tkinter import *
import tkinter.font as tkFont
from board import *
from client import *
from serveur import *
import threading
import webbrowser


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
        window.update() #update la fenêtre

def stop_buttons():
    """
    Empêche le clique des bouttons (cases) lors d'une partie
    :return:
    """
    for i in range(6):
        for j in range(7):
            button = buttons[i][j]
            button.configure(command=0)
    window.update()

def activate_buttons(lvl):
    """
    :paramètre lvl (indique si on joue en local, contre l'ordinateur ou en ligne).
    Permet de configurer la fonction lancée par les boutons lorsqu'on clique sur un bouton
    """
    for i in range(6):
        for j in range(7):
            button = buttons[i][j]
            if lvl == 0:
                button.configure(command=lambda row=i, col=j: on_button_click(row, col))
            elif lvl >= 1 and lvl <=3:
                button.configure(command=lambda row=i, col=j: on_button_click_ordi(row, col, lvl))
            elif lvl == 4 or lvl == 5:
                button.configure(command=lambda row=i, col=j: on_button_click_online(row, col, lvl))
            window.update()

def att_adversaire_joue_online(lvl):
    """
    :paramètre lvl (indique si on joue en local, contre l'ordinateur ou en ligne).
    en Online permet d'attendre que le joueur opposé est jouer pour reactiver les boutton et jouer à son tour
    """
    global tableau
    while True:
        if lvl == 4:
            coup_adversaire = get_data_serveur()
        elif lvl == 5:
            coup_adversaire = get_data_client()
        if coup_adversaire != None:
            coup_adversaire = int(coup_adversaire.decode())
            if lvl == 4:
                activate_buttons(4)
            elif lvl == 5:
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
                    break
                break
            break
    return


def on_button_click(row, col):
    """
    Paramètres : row et col qui sont la position du bouton dans la liste de boutons

    La fonction permet de faire jouer le joueur quand il clique sur un bouton et vérifie la possibilité de jouer
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
            afficher_gagnant(gagnant)


def on_button_click_online(row, col, lvl):
    """
    paramètres : row et col qui sont la position du bouton dans la liste de boutons
    ansi que lvl qui décrit si le joueur est client ou serveur

    La fonction permet de faire jouer le joueur quand il clique sur un bouton et vérifie la possibilité de jouer
    mais en ligne
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
        if lvl == 4:
            envoie_pos_joue_serveur(col)  # envoie à l'adversaire la pos jouée
        elif lvl == 5:
            envoie_pos_joue_client(col)   # envoie à l'adversaire la pos jouée
        stop_buttons()
        if gagnant is not None:
            afficher_gagnant(gagnant)
            return
        if lvl == 4:
            thread_attente_adversaire = threading.Thread(target=att_adversaire_joue_online, args=(lvl,))
        elif lvl == 5:
            thread_attente_adversaire = threading.Thread(target=att_adversaire_joue_online, args=(lvl,))
        thread_attente_adversaire.start()

def on_button_click_ordi(row, col, lvl):
    """
    Paramètres : row et col qui sont la position du boutons dans la liste de boutons
    ansi que lvl qui décrit qu'elle IA joue

    La fonction permet de faire jouer le joueur quand il clique sur un bouton et vérifie la possibilité de jouer
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
            afficher_gagnant(gagnant)
        else:
            if lvl == 1:
                tmp, gagnant = ordi_facile_joue(tableau)
            elif lvl == 2:
                tmp, gagnant = ordi_moyen_joue(tableau)
            elif lvl == 3:
                tmp, gagnant = ordi_difficile_joue(tableau)
            designe_joueur()
            if np.array_equal(tmp, tableau):
                tableau = tmp
            colorie_tableau(tableau)
            if gagnant is not None:
                stop_buttons()
                afficher_gagnant(gagnant)

def clear():
    """
    Efface tous les slaves de la window pour clear la fenêtre
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



def open_regle():
    webbrowser.open("https://www.regles.com/jeux/puissance-4.html")


def affiche_menu():
    """
    Affichage du menu principal
    """
    clear()
    title_label = Label(window, text="Menu", font=("Courier", 48), bg='#7092BE', fg='white', pady=30)
    title_label.grid(row=1, column=1, columnspan=3, sticky=EW)

    font_style = tkFont.Font(family='Courier', size=20)

    local_button = Button(window, text="Jouer en local", command=affiche_partie_locale, font=font_style,
                          width=20, pady=20, bd=0, highlightthickness=0)
    local_button.grid(row=2, column=2, columnspan=1, sticky=EW, pady=15)

    online_button = Button(window, text="Jouer en ligne", command=affiche_partie_en_ligne,
                           font=font_style, width=20, pady=20, bd=0, highlightthickness=0)
    online_button.grid(row=3, column=2, columnspan=1, sticky=EW, pady=15)

    rule_button = Button(window, text="Voir les règles", command=open_regle, font=font_style,
                         width=20, pady=20, bd=0, highlightthickness=0)
    rule_button.grid(row=4, column=2, columnspan=1, sticky=EW, pady=15)

    quit_button = Button(window, text="Quitter", command=window.destroy, pady=20, fg='black', bd=0,
                         highlightthickness=0, font=font_style)
    quit_button.grid(row=5, column=2, columnspan=1, sticky=EW, pady=35, padx=40)


def affiche_partie_locale():
    """
    Affichage du menu des parties en local
    soit jouer sur le même ordi ou jouer contre l'ordinateur
    """
    clear()
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
    """
    Affichage du menu des parties contre les ordinateurs
    """
    clear()
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
    """
    Affichage menu des parties en ligne
    Le joueur a le choix entre créer une partie et en rejoindre une
    """
    clear()
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
    """
    Affichage du menu une fois le serveur créé
    Attends la connection d'un joueur pour la thread pour lancer le jeu
    """
    clear()
    title_label = Label(window, text="En attente d'un joueur...", font=("Courrier", 48), bg='#7092BE', fg='white',
                        pady=30)
    title_label.grid(row=0, column=0)
    hostname = subprocess.check_output("hostname", shell=True).decode()
    hostname = hostname[:-2]
    IP = socket.gethostbyname(hostname)
    text_label = Label(window, text="IP du serveur :", font=("Courrier", 30), bg='#7092BE', fg='white', pady=30)
    text_label.grid(row=1, column=0)
    ip_label = Label(window, text=str(IP), font=("Courrier", 30), bg='#7092BE', fg='white', pady=30)
    ip_label.grid(row=1, column=1)
    thread_creer_partie = threading.Thread(target=creer_serveur)
    thread_lance_jeu = threading.Thread(target=jeu, args=(4,))
    thread_creer_partie.start()
    while is_there_connection() == None:
        window.update()
    thread_lance_jeu.start()

def affiche_rejoindre_partie_en_ligne():
    """
    Affichage du menu pour rejoindre une partie en mettant l'adresse ip de l'host
    """
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
    """
    lance la thread côté client pour se connecter à l'host
    puis lance une thread d'affichage du jeu
    """
    thread_rejoindre_partie = threading.Thread(target=connect, args=(ip,))
    thread_lance_jeu = threading.Thread(target=jeu, args=(5,))
    thread_rejoindre_partie.start()
    thread_lance_jeu.start()

def jeu(lvl):
    """
    :paramètre lvl (indique si on joue en local, contre l'ordinateur ou en ligne).
    Fonction d'affichage du jeu
    prend en paramètre lvl pour changer les boutons et/ou les désactiver
    """
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
        thread_attente_adversaire = threading.Thread(target=att_adversaire_joue_online, args=(lvl,))
        thread_attente_adversaire.start()
    window.grid_columnconfigure(1, weight=0)
    window.grid_columnconfigure(2, weight=0)
    window.grid_columnconfigure(3, weight=0)


def afficher_gagnant(joueur):
    """
    prend en paramètre le joueur actuel
    colorie le tableau
    attends 1.5 secondes pour montrer comment le joueur a gagné
    puis clear la fenêtre et affiche le gagnant ou le cas d'égalité
    et enfin lance la fonction pour réinitialiser la partie
    """
    colorie_tableau(tableau)
    window.update()
    time.sleep(1.5)
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
    """
    récupère le tableau et tour en variable global
    les remets à leurs valeurs initiales
    et lance la facontion pour réinitialiser le joueur
    """
    global tableau
    global tour
    tableau = np.zeros([6, 7])
    tour = 0
    reinitialiser_joueur()


def designe_joueur():
    """
    Détruit l'ancien 'Tour joueur : '
    récupère le joueur actuel et recrée le 'Tour joueur : '
    """
    for l, i in enumerate(window.slaves()): # boucle pour détruire 'Tour joueur : '
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
window.geometry("1080x720")
window.minsize(720, 480)
window.maxsize(1080, 720)
window.config(background='#7092BE')

#configuration des colonnes pour les menus
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

#liste de boutons qui seront les cases pour jouer
buttons = [[None for _ in range(7)] for _ in range(6)]

# Afficher la fenêtre sur le menu
affiche_menu()
window.mainloop()