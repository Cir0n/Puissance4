import numpy as np
import random
import requests


tableau = np.zeros([6, 7])
joueur = 1
tour = 0
coups_produits = ''
SERVER = 'https://connect4.gamesolver.org/solve?pos='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
}


def verification(tableau, joueur):
    """
    paramètres : tableau numpy de dimensions 6,7; le joueur actuel
    vérifie horizontalement, verticalement et en diagonale si le joueur a aligné 4 pions
    renvoie True si c'est le cas
    """
    # Vérifie horizontalement si 4 pions sont aligné
    for i in range(tableau.shape[1] - 3):
        for j in range(tableau.shape[0]):
            if tableau[j, i] == joueur and tableau[j, i + 1] == joueur and tableau[j, i + 2] == joueur and \
                    tableau[j, i + 3] == joueur:
                return True

    # Vérifie verticalement si 4 pions sont aligner
    for i in range(tableau.shape[1]):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i] == joueur and tableau[j + 2, i] == joueur and \
                    tableau[j + 3, i] == joueur:
                return True

    # Vérifie diagonal
    for i in range(tableau.shape[1] - 3):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i + 1] == joueur and tableau[j + 2, i + 2] == joueur and \
                    tableau[j + 3, i + 3] == joueur:
                return True

    # Vérifie autre diagonal
    for i in range(3, tableau.shape[1]):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i - 1] == joueur and tableau[j + 2, i - 2] == joueur and \
                    tableau[j + 3, i - 3] == joueur:
                return True


def egalite(tableau):
    """
    paramètres : tableau numpy de dimensions 6,7
    renvoie True si aucun des joueurs n'a gagné et que le tableau est plein, cas d'égalité
    """
    if not verification(tableau, 1) and (not verification(tableau, 2)) and tableau.min() != 0:
        return True
    return False


def validite(tableau, position_jouer):
    """
    paramètres : tableau numpy de dimensions 6,7; la position à jouer
    renvoie True si le joueur peut jouer sur une colonne
    """
    if tableau[0, position_jouer] == 0:
        return True
    return False


def jouer(t, entrerJoueur):
    """
    paramètres : la position à jouer; le joueur actuel; tableau numpy de dimensions 6,7
    renvoie la modification du tableau

    demande l'entrée du joueur
    vérifie que le joueur peut jouer la position
    regarde toute la colonne jusqu'à trouver un pion d'un joueur et de placer au dessus de celui-ci
    si la boucle ne trouve rien on met le pion en bas de la colonne
    """
    global joueur
    global tour
    global coups_produits
    if validite(t, entrerJoueur):
        for i in range(t.shape[0] - 1, -1, -1):  # Loop from the bottom of the column
            if t[i, entrerJoueur] == 0:
                t[i, entrerJoueur] = joueur
                coups_produits += str(entrerJoueur+1)
                tour += 1
                if tour >= 7:
                    if verification(t, joueur):
                        print("Joueur", joueur, "a gagné !")
                        return t, joueur
                    elif egalite(t):
                        print("Égalité !")
                        return t, "égalité"
                joueur = (2 if joueur == 1 else 1)
                return t, None
    else:
        print("position invalide")
    return t, None

def reinitialiser_joueur():
    global joueur
    global coups_produits
    joueur = 1
    coups_produits = ''

def get_joueur():
    return joueur

def set_joueur(j):
    global joueur
    joueur = j


def coup_gagnant(tableau, joueur):
    for i in range(7):
        tableau_tmp = np.array(tableau)
        if validite(tableau_tmp, joueur):
            for l in range(tableau_tmp.shape[0] - 1, -1, -1):
                if tableau_tmp[l, i] == 0:
                    tableau_tmp[l, i] = joueur
                    break
            if verification(tableau_tmp, joueur):
                return i
    return -1



def ordi_facile_joue(tableau):
    global joueur
    joueur = 2
    coups_possibles = []
    for i in range(tableau.shape[0]):
        if validite(tableau, i):
            coups_possibles.append(i)
    coup = coups_possibles[random.randint(0,len(coups_possibles)-1)]
    return jouer(tableau, coup)

def ordi_moyen_joue(tableau):
    global joueur
    joueur = 2
    coup_gagnant_ordi = coup_gagnant(tableau, joueur)
    coup_gagnant_adversaire = coup_gagnant(tableau, joueur-1)
    if coup_gagnant_ordi != -1:
        return jouer(tableau, coup_gagnant_ordi)
    elif coup_gagnant_adversaire != -1:
        return jouer(tableau, coup_gagnant_adversaire)
    else:
        coups_possibles = []
        for i in range(tableau.shape[0]):
            if validite(tableau, i):
                coups_possibles.append(i)
        coup = coups_possibles[random.randint(0, len(coups_possibles) - 1)]
        return jouer(tableau, coup)

def ordi_difficile_joue(tableau):
    global joueur
    joueur = 2
    req = SERVER + coups_produits
    x = requests.get(req, headers=headers).json()
    max = -np.inf
    coup = 0
    for i in range(len(x['score'])):
        if x['score'][i] >= max and x['score'][i] != 100:
            coup, max, = i, x['score'][i]
    return jouer(tableau, coup)



