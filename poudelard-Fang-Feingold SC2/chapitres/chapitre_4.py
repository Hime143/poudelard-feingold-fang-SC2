from univers.personnage import *
from utils.input_utils import *
from chapitres.chapitre_1 import porte_casse
from random import randint, choice
#Petite intro pour le chapitre 4 de la finale de Quidditch
def intro_4():
    print("La fin d'année approche et bien évidemment la fameuse la finale de Quidditch que tout le monde attend avec ardeur.\n Tu vois Hagrid s'approcher de toi avec un grand sourire.")
    if porte_casse:
        print("Hagrid : Hey, coucou {}, ça va ? Pas trop stressé j'espère?".format(joueur["Prenom"]))
        print("Je pense que ça devrait aller...en revanche ma pauvre porte je sais pas trop si elle va bien...")
    else:
        print("Pas trop ça va. Ma première compétition, j'ai hâte de voler et gagner des points!")

#Création des équipes de Quidditch
def creer_equipe(maison, data_maison, est_joueur=False, joueur=None):
    equipe_data = data_maison[maison]['joueurs']

    equipe = {
        'nom': maison,
        'score': 0,
        'a_marque': 0,
        'a_stoppe': 0,
        'attrape_vifdor': False,
        'joueurs': equipe_data.copy()
    }

    if est_joueur and joueur:
        nouvelle_liste = [joueur['nom'] + " (Attrapeur)"]

        for p in equipe_data:
            if "(Attrapeur)" not in p and "(Attrapeuse)" not in p:
                nouvelle_liste.append(p)

        equipe['joueurs'] = nouvelle_liste

    return equipe



#Tentative de marquer des buts de manière aléatoire entre 1 et 10
def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = randint(1, 10)
    #Si le nombre est supérieur ou égal à 6, le but est marqué
    if proba_but >= 6:
        #Si l'attaquant est le joueur principal, il marque le but
        if joueur_est_joueur:
            buteur = equipe_attaque['joueurs'][0]
        else:
            buteur = choice(equipe_attaque['joueurs'])
        equipe_attaque['score'] += 10
        equipe_attaque['a_marque'] += 1
        print(buteur + " marque un but pour " + equipe_attaque['nom'] + " ! (+10 points)")
    else:
        #Si le tir échoue, la défense bloque l'attaque
        equipe_defense['a_stoppe'] += 1
        print(equipe_defense['nom'] + " bloque l'attaque !")



def apparition_vifdor():
    proba = randint(1, 6)
    #Le Vif d'Or apparaît uniquement si le nombre est égal à 6
    if proba == 6:
        return True
    return False

"""Fonction pour savor quelle équipe attrape le vif d'or"""
def attraper_vifdor(e1, e2):
    gagnant = choice([e1, e2])
    gagnant['score'] += 150
    gagnant['attrape_vifdor'] = True
    print("Le Vif d'Or a été attrapé par " + gagnant['nom'] + " ! (+150 points)")
    return gagnant

"""Affichage des scores des deux maisons"""
def afficher_score(e1, e2):
    print("Score actuel :")
    print("→ " + e1['nom'] + " : " + str(e1['score']) + " points")
    print("→ " + e2['nom'] + " : " + str(e2['score']) + " points")
