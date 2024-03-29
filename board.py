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

    # Vérifie verticalement si 4 pions sont aligné
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


def jouer(board, entrerJoueur):
    """
    paramètres : la position à jouer ; le joueur actuel ; tableau numpy de dimensions 6,7
    renvoie la modification du tableau

    demande l'entrée du joueur
    vérifie que le joueur peut jouer la position
    regarde toute la colonne jusqu'à trouver un pion d'un joueur et de placer au dessus de celui-ci
    si la boucle ne trouve rien on met le pion en bas de la colonne
    """
    global joueur
    global tour
    global coups_produits
    if validite(board, entrerJoueur):
        for i in range(board.shape[0] - 1, -1, -1):  # Loop from the bottom of the column
            if board[i, entrerJoueur] == 0:
                board[i, entrerJoueur] = joueur
                coups_produits += str(entrerJoueur+1)
                tour += 1
                if tour >= 7:
                    if verification(board, joueur):
                        print("Joueur", joueur, "a gagné !")
                        return board, joueur
                    elif egalite(board):
                        print("Égalité !")
                        return board, "égalité"
                joueur = (2 if joueur == 1 else 1)
                return board, None
    else:
        print("position invalide")
    return board, None

def reinitialiser_joueur():
    """
    Remet le joueur à l'état initial
    """
    global joueur
    global coups_produits
    joueur = 1
    coups_produits = ''

def get_joueur():
    """
    return le joueur, 1 ou 2
    """
    return joueur

def set_joueur(j):
    """
    paramètre : un numéros de joueur (1 ou 2)
    Modifie le joueur
    :param j:
    """
    global joueur
    joueur = j


def coup_gagnant(tableau, joueur):
    """

    :paramètres : un tableau de jeu ; un joueur.

    :return: i, le coup gagnant ; -1 si pas de coup gagnant.
    """
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
    """
    :paramètre:  tableau
    IA niveau facile, elle récupère la liste des coups possibles et joue un coup aléatoire dans cette liste
    :return: le coup que l'IA doit jouer.
    """
    global joueur
    joueur = 2
    coups_possibles = []
    for i in range(tableau.shape[0]):
        if validite(tableau, i):
            coups_possibles.append(i)
    coup = coups_possibles[random.randint(0,len(coups_possibles)-1)]
    return jouer(tableau, coup)

def ordi_moyen_joue(tableau):
    """
    :paramètre tableau
    IA niveau moyen, vérifie si elle peu gagner, si oui, elle joue, sinon elle vérifie si l'adversaire peut gagner, si oui, elle le bloque, sinon elle joue aléatoiremet.
    :return: Le coup à jouer.
    """
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
    """
    :paramètre: tableau
    IA niveau difficile, elle utilise l'algorithme minimax avec une profondeur maximale, on utilise une API pour récupérer cette algorithme afin d'optimiser la latence de jeu.
    :return: le coup a jouer
    """
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



