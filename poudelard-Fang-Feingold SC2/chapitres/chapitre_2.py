from univers.maison import *
from univers.personnage import *
from utils.input_utils import *


def rencontrer_amis(joueur):
    print("Tu entends des coups à la porte, en ouvrant tu te retrouves nez à nez avec un garçon roux.", end="")
    input()
    print("Ron: Salut, moi je suis Ron Weasley, y’a plus de place dans les autres wagons, est-ce que je peux m’asseoir à côté de toi?", end="")
    input()
    choix = demander_choix(
        "Que réponds-tu?:",
        [
            "Tu le regarde, tu le juges puis tu réfléchis, et dit finalement : permission accordé",
            "Ouais bien sûr",
            "Un Weasley??? Sérieusement, tu veux t’asseoir ici? Bah non"
        ]
    )
    if choix == 1:
        print("Ron : Super merci")
        joueur["Attributs"]["intelligence"] += 1
    if choix == 2:
        print("Ron : Super merci")
        joueur["Attributs"]["loyauté"] += 1
        joueur["Attributs"]["courage"] += 1
    elif choix == 3:
        print("Ne t’inquiète pas un Weasley ça mord pas” et il s’installe et dit")
        joueur["Attributs"]["ambition"] += 1
    else:
        print("Tu verras Poudlard est la meilleure école de sorcellerie")

    print("Tu vois une fille qui entre avec quelques bouquins et qui se présente.\n Hermione : Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    choix = demander_choix(
        "Que réponds-tu?:",
        [
            "Bien évidemment je suis issu des {} nous somme très bien éduqués".format(joueur["Nom"]),
            "Moi un bouquin, nom prénom lire un bouquin? Nan je préfère faire des expériences!",
            "Oh c’est quoi? C’est intéressant? Ça se cuisine? Ah oui je m’appelle {} {}, enchantée!".format(
                joueur["Nom"], joueur["Prenom"]
            )
        ]
    )
    if choix == 1:
        print(
            "Hermione: Tu es donc {} {} ! Ta famille est super reconnue dans tout l’univer magique, j’ai lu un tas de livre à ton propos".format(
                joueur["Nom"], joueur["Prenom"]
            )
        )
        joueur["Attributs"]["intelligence"] += 1
        joueur["Attributs"]["ambition"] += 1
    if choix == 2:
        print(
            "Hermione : Enchantée {} {} ,Il faudrait que tu lises ce livre, il est très important pour notre apprentissage!".format(
                joueur["Nom"], joueur["Prenom"]
            )
        )
        joueur["Attributs"]["courage"] += 1
    if choix == 3:
        print(
            "Hermione : Voyons… un livre, {} {} tu as le mal des transports? Tu veux que j’aille voir le machiniste? ".format(
                joueur["Nom"], joueur["Prenom"]
            )
        )
        joueur["Attributs"]["loyauté"] += 1

    print("Puis un garçon à l'air de famille riche entra, il avait les cheveux blond et des yeux bleus.")
    input()
    print("Drago : C’est un honneur de rencontrer un membre des {}, je suis Drago Malefoy!".format(joueur["Nom"]))
    choix = demander_choix(
        "Que réponds-tu?",
        [
            "Un Malefoy, tout l’honneur est pour moi !",
            "Oh tu connais ma famille? Intéressant",
            "Oh, enchanté c’est un honneur pour moi aussi de te rencontrer",
            "Peu importe la famille, je suis là pour faire des expériences inédites"
        ]
    )
    if choix == 1 or choix == 3:
        print("Je suis ravi de te connaître, j’espère qu’on pourra renforcer le pouvoir de nos deux familles ensemble")
        joueur["Attributs"]["ambition"] += 1
        joueur["Attributs"]["loyauté"] += 1
    if choix == 2:
        print("Un Malfoy qui ne connaît pas la famille la plus influente de tout l’univers magique? Ce serait une honte!")
        joueur["Attributs"]["intelligence"] += 1
    if choix == 4:
        print("Des expériences? Tu dois en pratiquer souvent au domaine Bluebell")
        joueur["Attributs"]["courage"] += 1






def mot_de_bienvenue():
    print("Dumbledore: \n Bienvenue à Poudlard pour cette nouvelle année ! Avant de commencer le banquet, j'aimerais dire quelques mots.\n Voici nos nouveaux élèves, qui vont être répartis par le Choixpeau. Comme vous le savez chaque année la forêt interdite est interdite aux élèves. \n Cette année, les toilettes situées dans les cachots seront condamnées d’accès. Bien, commençons la répartition!")


def ceremonie_repartition(joueur):
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie",
             "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]

    print("La cérémonie de répartition commence dans la Grande Salle...")
    print("Le professeur McGonagall t'appelle, tu entends des chuchotements et tu t’avances avant de t’asseoir sur le tabouret.")
    print("Le Choixpeau se pose sur ta tête et tu sens des questions traverser ton esprit...")
    input()

    maison = repartition_maison(joueur, questions)

    joueur["Maison"] = maison

    print("Le Choixpeau s’exclame : {} !!!".format(maison))
    print("Tu rejoins les élèves de {} sous les acclamations !".format(maison))


def installation_salle_commune(joueur):
    maisons = load_fichier("../data/maisons.json")

    maison = joueur["Maison"]
    info = maisons[maison]

    print("Vous suivez les préfets à travers les couloirs du château...")
    print(info["emoji"], info["description"])
    print(info["message_installation"])
    print("Les couleurs de votre maison :", ", ".join(info["couleurs"]))

def lancer_chapitre_2(joueur):
    rencontrer_amis(joueur)
    print("Après quelques heures de train, tu vois enfin le majestueux château de l’école de sorcellerie Poudlard.")
    input()
    print("Vous descendez et vous êtes guidés par Hagrid vers des barques.\n Vous faites la traversée du lac et vous vous retrouvez bientôt dans une grande salle remplie de bougies flottantes et d’autres élèves sorciers.\n Tu vois un drôle de chapeau au centre de la salle")
    mot_de_bienvenue()
    input()
    ceremonie_repartition(joueur)
    input()
    print("Après le banquet, tu suis ton préfet de maison pour aller dans la salle commune de {}...".format(joueur["Maison"]))
    installation_salle_commune(joueur)
    input()
    afficher_personnage(joueur)
    input()
    print("Fin du Chapitre 2 — Les cours vont bientôt commencer à Poudlard !")

lancer_chapitre_2(joueur)