from tkinter import *
import numpy as np

b = np.zeros([6, 7])


def verification(tableau, joueur):
    # Vérifie horizontalement si 4 pions sont aligné
    for i in range(tableau.shape[1] - 3):
        for j in range(tableau.shape[0]):
            if tableau[j, i] == joueur and tableau[j, i + 1] == joueur and tableau[j, i + 2] == joueur and tableau[
                j, i + 3] == joueur:
                print(f'joueur {joueur} a gagné')
                return True
    # Vérifie verticalement si 4 pions sont aligner
    for i in range(tableau.shape[1]):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i] == joueur and tableau[j + 2, i] == joueur and tableau[
                j + 3, i] == joueur:
                print(f'joueur {joueur} a gagné')
                return True
    # Vérifie diagonal
    for i in range(tableau.shape[1] - 3):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i + 1] == joueur and tableau[j + 2, i + 2] == joueur and \
                    tableau[j + 3, i + 3] == joueur:
                print(f'joueur {joueur} a gagné')
                return True
    # Vérifie autre diagonal
    for i in range(3, tableau.shape[1]):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i - 1] == joueur and tableau[j + 2, i - 2] == joueur and \
                    tableau[j + 3, i - 3] == joueur:
                print(f'joueur {joueur} a gagné')
                return True

def validite(tableau,position_jouer):
    if tableau[0, position_jouer] == 0:
        return True
    return False

def jouer(position_jouer, joueur, tableau):
    if validite(tableau, position_jouer):
        for i in range(tableau.shape[0] - 1):
            if tableau[i + 1, position_jouer] != 0:
                tableau[i, position_jouer] = joueur
                return tableau
        tableau[5, position_jouer] = joueur
        return tableau
