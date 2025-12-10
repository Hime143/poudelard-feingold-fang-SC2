from utils.input_utils import demander_choix


def rencontrer_amis(joueur):
    print("Tu entends des coups à la porte, en ouvrant tu te retrouves nez à nez avec un garçon roux.", end="")
    input()
    print("Ron: Salut, moi je suis Ron Weasley, y’a plus de place dans les autres wagons, est-ce que je peux m’asseoir à côté de toi?", end="")
    input()
    choix = demander_choix("Que réponds-tu?:", ["Tu le regarde, tu le juges puis tu réfléchis, et dit finalement : permission accordé", "Ouais bien sûr","Un Weasley??? Sérieusement, tu veux t’asseoir ici? Bah non"])
    if choix == 1 or choix == 2:
        print("Ron : Super merci")
    elif choix == 3:
        print("Ne t’inquiète pas un Weasley ça mord pas” et il s’installe et dit")
    else:
        print("Tu verras Poudlard est la meilleure école de sorcellerie")

    print("Tu vois une fille qui entre avec quelques bouquins et qui se présente.\n Hermione : Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    choix = demander_choix("Que réponds-tu?:",["Bien évidemment je suis issu des {} nous somme très bien éduqués"])