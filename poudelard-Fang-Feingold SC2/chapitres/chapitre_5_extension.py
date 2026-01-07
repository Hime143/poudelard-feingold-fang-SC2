from utils.input_utils import *
from univers.maison import *
from random import choice



def choisir_potion():
    potions = load_fichier("./data/potion.json")
    nom_potion = choice(list(potions.keys()))
    potion = potions[nom_potion]
    potion["nom"] = nom_potion
    return potion

def preparer_potion(joueur):
    potion = choisir_potion()
    print("Tu entres dans la salle de potions, les chaudrons bouillonnent et une légère vapeur magique flotte dans l'air.")
    input()
    print("Tu te hâtes et te met devant ton chaudron.")
    input()
    print("Le professeur regarde les élèves dans la salle et dit : Aujourd'hui, nous allons préparer la potion {}. Soyez rigoureux et attentif ! ".format(potion["nom"]))
    input()
    print("Tu observes les ingrédients étalés devant toi : chaque détails compte pour réussir la potion.")
    input()
    print(" Description : {}".format(potion["description"]))

    ingredients_attendus = potion["ingredients"]
    ingredients_joueur = []
    nb_correct = 0

    print("\n Commence à ajouter les ingrédients dans le bon ordre pour réussir la potion.\n")

    for i in range(len(ingredients_attendus)):
        ingr = input("Ingrédient n°{} : ".format(i + 1))
        ingredients_joueur.append(ingr)

        if ingr == ingredients_attendus[i]:
            print("{} ajouté correctement !".format(ingr))
            nb_correct += 1
            print("Le chaudron bouillonne harmonieusement…")
        else:
            print("{} est incorrect… Le chaudron grésille !".format(ingr))
        input()

    print()


    if nb_correct == len(ingredients_attendus):
        print(" Le chaudron s'illumine et une lueur magique s'élève !")
        input()
        print("Tu regardes avec satisfaction les couleurs émanant du chaudron")
        input()
        print("Le professeur sourit : Excellent travail ! Cette potion est parfaite ! Vous excellez dans l'art des potions {} {}!".format(joueur["Nom"],joueur["Prenom"]))
        joueur["score"] += 50
    else:
        print(" Le chaudron émet une fumée noire… la potion a mal tourné.")
        input()
        print("Tu te retrouves avec de la suie sur ton visage...")
        input()
        print("L'ordre correct des ingrédients était : {}".format(ingredients_attendus))
        input()
        print("Le professeur te regarde et dit: il faut travailler davantages vos leçon de potion {} {}".format(joueur["Nom"], joueur["Prenom"]))
        input()


def lancer_chapitre_5(joueur, maisons):
    print("Chapitre 5 - Le cours de potion")
    preparer_potion(joueur)
    actualiser_points_maison(maisons, joueur["Maison"], joueur["score"])
    print("\n Points actuels pour {} : {}".format(joueur["Maison"], joueur["score"]))
    input("Tu prends une grande inspiration et observes le résultat de ton travail...\n")
    print("Fin du Chapitre 5")
