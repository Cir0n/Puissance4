from board import *

tableau = np.zeros([6, 7])
joueur = 1
tour = 0


print(tableau)
while True :
    print(f'tour joueur {joueur} : ')
    entrerJoueur = int(input("entrer colonne : "))
    tableau = jouer(entrerJoueur, joueur,tableau)
    print(tableau)
    tour += 1
    if tour >= 8:
        if verification(tableau, joueur):
            break
    joueur = (2 if joueur == 1 else 1)
