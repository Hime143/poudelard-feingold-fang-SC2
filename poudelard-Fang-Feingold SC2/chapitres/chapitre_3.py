from univers.maison import *
from univers.personnage import *
from utils.input_utils import *
from random import choice

#fonction pour apprendre 5 sort 1 offensif, 1 defensif et 3 utilitaires, description des 5 osrts
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

#quizz sur 4 sorts au hasard, le joueur doit donner leur nom à partir d'une description
def quiz_magie(joueur):
    print("Bienvenue au quiz de magie de Poudlard !\nRéponds correctement aux 4 questions pour faire gagner des points à ta maison.")
    questions = []
    f = load_fichier("./data/quiz_magie.json")
    while len(questions) < 4:
        question = choice(f)
        if question not in questions:
            questions.append(question)
    score = 0
    for question in questions:
        print(question["question"])
        reponse = input()
        if reponse == question["reponse"]:
            print("Bonne réponse ! +25 points pour ta maison.")
            score += 25
        else:
            print("Mauvaise réponse. La bonne réponse était : {}".format(question["reponse"]))
    print("score obtenue : {} points".format(score))
    joueur["score"] = score

#fonction du chapitre 3 ensemble, ajout des points dans la maison du joueur et transition entre chapitre 3 et 4
def lancer_chapitre_3(joueur,maisons):
    apprendre_sort(joueur)
    input()
    quiz_magie(joueur)
    actualiser_points_maison(maisons, joueur["Maison"], joueur["score"])
    input()
    print("la maison en tête pour l'instant est :",end="")
    afficher_maison_gagnante(maisons)
    input()
    afficher_personnage(joueur)
    input()
    print("Fin du Chapitre 3 —")
