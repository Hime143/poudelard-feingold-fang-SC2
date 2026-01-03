from utils.input_utils import *
from chapitres.chapitre_1 import *
from chapitres.chapitre_2 import *
from chapitres.chapitre_3 import *
from chapitres.chapitre_4 import *
from chapitres.chapitre_5_extension import *

def afficher_menu_principal():
    print("1. Lancer le Chapitre 1 – L’arrivée dans le monde magique.\n2. Quitter le jeu.")
def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
    choix = 0
    while not choix == (1 or 2):
        afficher_menu_principal()
        choix = int(input())
        if choix == 1:
            joueur = initialiser()
            lancer_chapitre_1(joueur)
            lancer_chapitre_2(joueur,maisons)
            lancer_chapitre_3(joueur, maisons)
            lancer_chapitre_4(joueur, maisons)
            lancer_chapitre_5(joueur, maisons)
        elif choix == 2:
            print("A bientôt à Poudelard")
            quit()
        else:
            print("Erreur, choix invalide")