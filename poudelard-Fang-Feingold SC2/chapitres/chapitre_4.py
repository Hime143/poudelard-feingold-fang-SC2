import json
from univers.personnage import *
from utils.input_utils import *
from univers.maison import *
from chapitres.chapitre_1 import porte_casse
from random import randint, choice

# Intro du chapitre 4
def intro_4(joueur):
    print("La fin d'année approche et bien évidemment la fameuse finale de Quidditch que tout le monde attend avec ardeur.\nTu vois Hagrid s'approcher de toi avec un grand sourire.")
    if porte_casse:
        print("Hagrid : Hey, coucou {}, ça va ? Pas trop stressé j'espère?".format(joueur["Prenom"]))
        print("Je pense que ça devrait aller...en revanche ma pauvre porte je sais pas trop si elle va bien...")
    else:
        print("Pas trop ça va. Ma première compétition, j'ai hâte de voler et gagner des points!")

# Création des équipes
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

# Tentative de but
def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = randint(1, 10)
    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque['joueurs'][0]
        else:
            buteur = choice(equipe_attaque['joueurs'])
        equipe_attaque['score'] += 10
        equipe_attaque['a_marque'] += 1
        print(buteur + " marque un but pour " + equipe_attaque['nom'] + " ! (+10 points)")
    else:
        equipe_defense['a_stoppe'] += 1
        print(equipe_defense['nom'] + " bloque l'attaque !")

# Apparition du Vif d'Or
def apparition_vifdor():
    return randint(1, 6) == 6

# Capture du Vif d'Or
def attraper_vifdor(e1, e2):
    gagnant = choice([e1, e2])
    gagnant['score'] += 150
    gagnant['attrape_vifdor'] = True
    print("Le Vif d'Or a été attrapé par " + gagnant['nom'] + " ! (+150 points)")
    return gagnant

# Affichage du score
def afficher_score(e1, e2):
    print("Score actuel :")
    print("→ " + e1['nom'] + " : " + str(e1['score']) + " points")
    print("→ " + e2['nom'] + " : " + str(e2['score']) + " points")

# Affichage d'une équipe
def afficher_equipe(maison, equipe):
    print("Équipe de " + maison + " :")
    for joueur in equipe['joueurs']:
        print("- " + joueur)

# Déroulement complet du match
def match_quidditch(joueur, maisons):
    fichier = load_fichier("./data/equipes_quidditch.json")
    maison_joueur = joueur['maison']
    maisons_adverses = list(data_maison.keys())
    maisons_adverses.remove(maison_joueur)
    maison_adverse = choice(maisons_adverses)

    print("\nMatch de Quidditch : " + maison_joueur + " vs " + maison_adverse + " !")
    equipe_joueur = creer_equipe(maison_joueur, data_maison, True, joueur)
    equipe_adverse = creer_equipe(maison_adverse, data_maison)

    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adverse)

    print("Tu joues pour " + maison_joueur + " en tant qu’Attrapeur")

    for tour in range(1, 21):
        print("\n━━━ Tour " + str(tour) + " ━━━")
        tentative_marque(equipe_adverse, equipe_joueur)
        tentative_marque(equipe_joueur, equipe_adverse, True)
        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor():
            print("Le Vif d'Or apparaît !")
            gagnant_vifdor = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("Fin du match !")
            break

        input("Appuyez sur Entrée pour passer au tour suivant...")

    print("\nScore final :")
    afficher_score(equipe_joueur, equipe_adverse)

    if equipe_joueur['score'] > equipe_adverse['score']:
        gagnant = equipe_joueur
    elif equipe_adverse['score'] > equipe_joueur['score']:
        gagnant = equipe_adverse
    else:
        print("Match nul ! Aucun point attribué.")
        return

    if equipe_joueur['attrape_vifdor']:
        print(equipe_joueur['nom'] + " a attrapé le Vif d'Or ! +150 points")
    elif equipe_adverse['attrape_vifdor']:
        print(equipe_adverse['nom'] + " a attrapé le Vif d'Or ! +150 points")

    print("La maison gagnante est " + gagnant['nom'] + " avec " + str(gagnant['score']) + " points !")
    actualiser_points_maison(maisons, gagnant['nom'], 500)
    print("+500 points pour " + gagnant['nom'] + " !")

# Lancer le chapitre 4 complet
def lancer_chapitre4(joueur, maisons):
    print("Chapitre 4 : Finale de Quidditch")
    intro_4(joueur)
    match_quidditch(joueur, maisons)
    print("Fin du Chapitre 4 — Quelle performance incroyable sur le terrain !")
    print("La maison qui remporte la Coupe des Quatre Maisons est :", end=" ")
    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)
    print("Fin du Chapitre 4 !")
