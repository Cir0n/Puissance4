import numpy as np

tableau = np.zeros([6, 7])
joueur = 1
tour = 0


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


def jouer(tableau, entrerJoueur):
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
    if validite(tableau, entrerJoueur):

        for i in range(tableau.shape[0] - 1, -1, -1):  # Loop from the bottom of the column
            if tableau[i, entrerJoueur] == 0:
                tableau[i, entrerJoueur] = joueur
                tour += 1
                if tour >= 7:
                    if verification(tableau, joueur):
                        print("Joueur", joueur, "a gagné !")
                        return tableau, joueur
                    elif egalite(tableau):
                        print("Égalité !")
                        return tableau, None
                joueur = (2 if joueur == 1 else 1)
                return tableau, None
        print("colonne pleine")
    else:
        print("position invalide")
    return tableau, None




