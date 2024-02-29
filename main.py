from board import *
from affichage import *
import os

tableau = np.zeros([6, 7])
joueur = 1
tour = 0

# Configurations de la fenetre puissance 4
window = Tk()
window.title("Puissance 4")
window.iconbitmap("image/puissance4.ico")
window.geometry("1080x720")
window.minsize(720, 480)
window.config(background='#7092BE')

affiche_menu(window)
# Afficher la fenêtre
window.mainloop()

print(tableau)
while True:
    print('tour joueur', joueur)
    while True:
        try:
            entrerJoueur = int(input("entrer colonne : "))
            break
        except ValueError:
            print("Veuillez entrer une colonne Valide")

    tableau = jouer(entrerJoueur, joueur, tableau)
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
