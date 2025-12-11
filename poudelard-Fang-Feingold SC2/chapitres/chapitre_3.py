from univers.maison import *
from univers.personnage import *
from utils.input_utils import *
from random import choice

def apprendre_sort(joueur):
    print("Tu te réveilles de bon matin, c’est ta première journée de cours. Tu regardes alors ton emploi du temps et tu vois que tu as cours de Sortilèges aujourd’hui.\nTu te prépares avant de prendre ton sac et de te diriger vers la salle du cours de Sortilèges. Tu t’installes et ouvre ton livre de sortilèges.",end="")
    input()
    nb_off = 0
    nb_util = 0
    nb_deff = 0
    f = load_fichier("./data/sorts.json")
    while (nb_off < 1) or (nb_deff < 1) or (nb_util < 3):
        sort = choice(f)
        if sort["type"] == "Utilitaire" and sort["nom"] not in joueur["Sortilèges"]:
            if nb_util < 3:
                ajouter_objet(joueur,"Sortilèges",sort["nom"])
                print("bravo tu as appris {},({})".format(sort["nom"],sort["type"]),end="")
                nb_util += 1
                input()
        elif sort["type"] == "Défensif":
            if nb_deff < 1:
                ajouter_objet(joueur,"Sortilèges",sort["nom"])
                print("bravo tu as appris {},({})".format(sort["nom"],sort["type"]),end="")
                nb_deff += 1
                input()
        else:
            if nb_off < 1:
                ajouter_objet(joueur,"Sortilèges",sort["nom"])
                print("bravo tu as appris {},({})".format(sort["nom"],sort["type"]),end="")
                nb_off += 1
                input()

    print("Voici les sorts que tu maîtrises désormais!")
    for i in range(len(joueur["Sortilèges"])):
        for j in f:
            if j["nom"] == joueur["Sortilèges"][i]:
                print("-{} ({}) : {}".format(j["nom"],j["type"],j["description"]))

