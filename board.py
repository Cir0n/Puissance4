import numpy as np

b = np.zeros([6, 7])


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
                print('joueur', joueur, 'a gagné')
                return True

    # Vérifie verticalement si 4 pions sont aligner
    for i in range(tableau.shape[1]):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i] == joueur and tableau[j + 2, i] == joueur and \
                    tableau[j + 3, i] == joueur:
                print('joueur', joueur, 'a gagné')
                return True

    # Vérifie diagonal
    for i in range(tableau.shape[1] - 3):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i + 1] == joueur and tableau[j + 2, i + 2] == joueur and \
                    tableau[j + 3, i + 3] == joueur:
                print('joueur', joueur, 'a gagné')
                return True

    # Vérifie autre diagonal
    for i in range(3, tableau.shape[1]):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i - 1] == joueur and tableau[j + 2, i - 2] == joueur and \
                    tableau[j + 3, i - 3] == joueur:
                print(f'joueur', joueur, 'a gagné')
                return True


def egalite(tableau):
    if not verification(tableau, 1) and (not verification(tableau, 2)) and tableau.min() != 0:
        print("Égalité !")
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


def jouer(position_jouer, joueur, tableau):
    """
    paramètres : la position à jouer; le joueur actuel; tableau numpy de dimensions 6,7
    renvoie la modification du tableau

    vérifie que le joueur peut jouer la position
    regarde toute la colonne jusqu'à trouver un pion d'un joueur et de placer au dessus de celui-ci
    si la boucle ne trouve rien on met le pion en bas de la colonne
    """
    if validite(tableau, position_jouer):
        for i in range(tableau.shape[0] - 1):
            if tableau[i + 1, position_jouer] != 0:
                tableau[i, position_jouer] = joueur
                return tableau
        tableau[5, position_jouer] = joueur
        return tableau
    return tableau
