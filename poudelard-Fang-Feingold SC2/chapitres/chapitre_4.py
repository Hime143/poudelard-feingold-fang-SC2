from univers.maison import *
from univers.personnage import *
from utils.input_utils import *
from random import randint, choice
from chapitres.chapitre_1 import is_porte_casse


def intro_4(joueur):
    print("La fin d'année approche et bien évidemment la fameuse finale de Quidditch que tout le monde attend avec ardeur.")
    print("Tu vois Hagrid s'approcher de toi avec un grand sourire.")
    input()
    if is_porte_casse():
        print("Hagrid : Hey, coucou {}, ça va ? Pas trop stressé j'espère ?".format(joueur["Prenom"]))
        input()
        print("Je pense que ça devrait aller... en revanche ma pauvre porte je sais pas trop si elle va bien...")
    else:
        print("Pas trop, ça va. Ma première compétition, j'ai hâte de voler et gagner des points !")
    input()


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe_data = equipe_data[maison]['joueurs']
    equipe = {
        'nom': maison,
        'score': 0,
        'a_marque': 0,
        'a_stoppe': 0,
        'attrape_vifdor': False,
        'joueurs': equipe_data.copy()
    }

    if est_joueur and joueur:
        nouvelle_liste = [joueur['Nom'] + " (Attrapeur)"]
        for p in equipe_data:
            if "(Attrapeur)" not in p and "(Attrapeuse)" not in p:
                nouvelle_liste.append(p)
        equipe['joueurs'] = nouvelle_liste

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = randint(1, 10)
    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque['joueurs'][0]
        else:
            buteur = choice(equipe_attaque['joueurs'])
        equipe_attaque['score'] += 10
        equipe_attaque['a_marque'] += 1
        print("{} marque un but pour {} ! (+10 points)".format(buteur, equipe_attaque['nom']))
    else:
        equipe_defense['a_stoppe'] += 1
        print("{} bloque l’attaque !".format(equipe_defense['nom']))


# Apparition et capture du Vif d'Or

def apparition_vifdor():
    return randint(1, 6) == 6

def attraper_vifdor(e1, e2):
    gagnant = choice([e1, e2])
    gagnant['score'] += 150
    gagnant['attrape_vifdor'] = True
    print("Le Vif d’Or a été attrapé par {} ! (+150 points)".format(gagnant['nom']))
    return gagnant

# Affichage du score et équipes

def afficher_score(e1, e2):
    print("Score actuel :")
    print("→ {} : {} points".format(e1['nom'], e1['score']))
    print("→ {} : {} points".format(e2['nom'], e2['score']))

def afficher_equipe(maison, equipe):
    print("Équipe de {} :".format(maison))
    for joueur in equipe['joueurs']:
        print("- " + joueur)


# Déroulement complet du match

def match_quidditch(joueur, maisons):
    fichier = load_fichier("./data/equipes_quidditch.json")
    maison_joueur = joueur['Maison']
    maisons_adverses = list(maisons.keys())
    maisons_adverses.remove(maison_joueur)
    maison_adverse = choice(maisons_adverses)

    print("Match de Quidditch : {} vs {} !".format(maison_joueur, maison_adverse))
    equipe_joueur = creer_equipe(maison_joueur, fichier, True, joueur)
    equipe_adverse = creer_equipe(maison_adverse, fichier)

    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adverse)

    print("Tu joues pour {} en tant qu’Attrapeur".format(maison_joueur))
    input()

    gagnant_vifdor = None  # Initialisation pour utilisation après la boucle

    # Boucle de 20 tours maximum
    for tour in range(1, 21):
        print("\n━━━ Tour {} ━━━".format(tour))

        tentative_marque(equipe_adverse, equipe_joueur)
        tentative_marque(equipe_joueur, equipe_adverse, True)

        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor():
            print("\nLe Vif d’Or apparaît !")
            gagnant_vifdor = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("Fin du match !")
            break

        input()

    # Score final
    print("\nScore final :")
    afficher_score(equipe_joueur, equipe_adverse)

    # Affichage du gagnant du Vif d'Or si attrapé
    if gagnant_vifdor:
        print("Le Vif d’Or a été attrapé par {} !".format(gagnant_vifdor['nom']))

    # Détermination du gagnant du match
    if equipe_joueur['score'] > equipe_adverse['score']:
        gagnant_match = equipe_joueur
    elif equipe_adverse['score'] > equipe_joueur['score']:
        gagnant_match = equipe_adverse
    else:
        print("Match nul ! Aucun point attribué.")
        return

    print("La maison gagnante est {} avec {} points !".format(gagnant_match['nom'], gagnant_match['score']))
    actualiser_points_maison(maisons, gagnant_match['nom'], 500)
    print("+500 points pour {} !".format(gagnant_match['nom']))

# Lancer le chapitre 4 complet

def lancer_chapitre_4(joueur, maisons):
    print("Chapitre 4 : Finale de Quidditch")
    intro_4(joueur)
    match_quidditch(joueur, maisons)
    print("Fin du Chapitre 4 — Quelle performance incroyable sur le terrain !")
    print("La maison qui remporte la Coupe des Quatre Maisons est :", end=" ")
    afficher_maison_gagnante(maisons)
    input()
    afficher_personnage(joueur)
    print("Fin du Chapitre 4 !")
