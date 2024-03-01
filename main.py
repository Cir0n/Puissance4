from board import *
from affichage import *

import os

tableau = np.zeros([6, 7])
joueur = 1
tour = 0

print(tableau)
while True:
    print('tour joueur', joueur)

    tableau = jouer(joueur, tableau)
    os.system('cls')
    print(tableau)
    tour += 1
    if tour >= 7:
        if verification(tableau, joueur):
            print("Joueur ", joueur, " a gagné !")
            break
        elif egalite(tableau):
            print("Égalité !")
            break
    joueur = (2 if joueur == 1 else 1)
