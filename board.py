from tkinter import *
import numpy as np

b = np.zeros([6, 7])


def verification(tableau, joueur):
    # Vérifie horizontalement si 4 pions sont aligné
    for i in range(tableau.shape[1] - 3):
        for j in range(tableau.shape[0]):
            if tableau[j, i] == joueur and tableau[j, i + 1] == joueur and tableau[j, i + 2] == joueur and tableau[j, i + 3] == joueur:
                print(f'joueur {joueur} a gagné')
                return True
    # Vérifie verticalement si 4 pions sont aligner
    for i in range(tableau.shape[1]):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i] == joueur and tableau[j + 2, i] == joueur and tableau[j + 3, i] == joueur:
                print(f'joueur {joueur} a gagné')
                return True
    # Vérifie diagonal
    for i in range(tableau.shape[1] - 3):
        for j in range(tableau.shape[0] - 3):
            if tableau[j, i] == joueur and tableau[j + 1, i + 1] == joueur and tableau[j + 2, i + 2] == joueur and tableau[j + 3, i + 3] == joueur:
                print(f'joueur {joueur} a gagné')
                return True
    # Vérifie autre diagonal
    for i in range(3, tableau.shape[1]):
        for j in range(tableau.shape[0]):
            if tableau[j, i] == joueur and tableau[j + 1, i - 1] == joueur and tableau[j + 2, i - 2] == joueur and tableau[j + 3, i - 3] == joueur:
                print(f'joueur {joueur} a gagné')
                return True



assert verification(np.array(
    [[0, 1, 0, 0, 1, 1, 1],
     [1, 1, 1, 1, 2, 0, 0],
     [1, 1, 2, 2, 1, 0, 0],
     [2, 2, 1, 2, 1, 1, 2],
     [0, 2, 1, 2, 1, 2, 1],
     [2, 1, 1, 1, 2, 2, 1]]), 1), "Condition 1 horiz"

assert verification(np.array(
    [[0, 1, 0, 0, 1, 1, 1],
     [1, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 2, 2, 2, 2, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]), 2), "Condition 2 horiz"

assert verification(np.array(
    [[0, 1, 0, 0, 1, 1, 1],
     [1, 0, 2, 1, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]), 2), "Condition 1 verti"

assert verification(np.array(
    [[0, 1, 0, 0, 1, 1, 1],
     [1, 1, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 1, 1, 0],
     [0, 1, 1, 1, 2, 0, 0],
     [0, 1, 2, 2, 2, 0, 0]]), 1), "Condition 2 verti"

assert verification(np.array(
    [[2, 1, 0, 1, 1, 1, 0],
     [1, 2, 0, 0, 0, 0, 0],
     [0, 1, 2, 0, 0, 0, 0],
     [0, 0, 2, 2, 0, 1, 0],
     [0, 2, 2, 2, 1, 0, 0],
     [0, 0, 0, 1, 1, 0, 0]]), 2), "Condition 1 diago"

assert verification(np.array(
    [[0, 1, 0, 1, 1, 1, 0],
     [1, 1, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 1],
     [0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]), 1), "Condition 2 diago"

assert verification(np.array(
    [[0, 1, 0, 0, 1, 1, 1],
     [1, 0, 1, 1, 0, 2, 0],
     [0, 0, 0, 0, 2, 0, 0],
     [0, 0, 0, 2, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]), 2), "Condition 3 diago"
