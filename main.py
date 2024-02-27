from board import *
from affichage import *
import os

tableau = np.zeros([6, 7])
joueur = 1
tour = 0


print(tableau)
while True:
    print('tour joueur', joueur)
    while True:
        try:
            entrerJoueur = int(input("entrer colonne : "))
            break
        except ValueError:
            print("Veuillez entrer une colonne Valide")

    tableau = jouer(entrerJoueur, joueur,tableau)
    os.system('cls')
    print(tableau)
    tour += 1
    if tour >= 8:
        if verification(tableau, joueur):
            break
    joueur = (2 if joueur == 1 else 1)
