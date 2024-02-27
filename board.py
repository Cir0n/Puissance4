from tkinter import *
import numpy as np


def verification(tableau):
    b = np.zeros([6, 7])
    # Vérifie horizontalement si 4 pions sont aligné
    for i in range(b.shape[1] - 3):
        for j in range(b.shape[0]):
            if b[j][i] == 1 and b[j][i + 1] == 1 and b[j][i + 2] == 1 and b[j][i + 3] == 1:
                return True
    # Vérifie verticalement si 4 pions sont aligner
    for i in range(b.shape[1]):
        for i in range(b.shape[0] - 3):
            if b[j][i] == 1 and b[j + 1][i] == 1 and b[j + 2][i] == 1 and b[j + 3][i] == 1:
                return True
    # Vérifie diagonal
    for i in range(b.shape[1] - 3):
        for j in range(b.shape[0] - 3):
            if b[j][i] == 1 and b[j + 1][i + 1] == 1 and b[j + 2][i + 2] == 1 and b[j + 3][i + 3] == 1:
                return True
    #verif autre diagonale
    for i in range (b.shape[1]-3):
        for j in range(3, b.shape[0]):
            if b[]














