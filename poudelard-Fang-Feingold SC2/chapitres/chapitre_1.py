from main import joueur
from utils.input_utils import demander_choix


def introduction():
    print("Bienvenue en 1990... 10 ans depuis la disparition de Lord Voldemort.",end="")
    input()
    print("Issu d'une famille puissante de sorciers, tu atteins l'âge de tes 11 ans et tu t'apprêtes à faire ta rentrée à Poudlard.",end="")
    input()
    print("Tu attends ta lettre d'acceptation pour t'aventurer sur le Chemin de Traverse...")
    input()

def recevoir_lettre():
    print("Tu vois une chouette traverser la fenêtre et qui t’apporte une lettre scellée du sceau de Poudlard... ",end="")
    input()
    print("« Cher élève, Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »",end="")
    input()
    choix =demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",["Oui","Non"])
    if choix == 2:
        print("Tu as choisi de refuser…ALORS QUE TU ES ISSUS D’UNE PUISSANTE FAMILLE DE SORCIER??? Tu as été renier par ta famille…Fin du jeu")
        quit()
    else:
        print("Tu as choisi d’accepter d’aller à Poudlard, bienvenue jeune élève dans le monde des sorciers!")
        input()

porte_casse = False
def coucouHagrid():
    print("Toc,toc...Tu te lèves pour aller ouvrir, tu tombes nez à nez avec un géant de plus de 2m et demi.",end="")
    input()
    choix = demander_choix("Surpris tu:",["*Tu recules de 5m*","demandes: -Bonjour, puis-je vous aider Monsieur..?","*claques la porte au nez*","dit: c'est vous le livreur de pizza? Vous êtes très en retard..."])
    if choix == 1 or choix == 2:
        print("Bonjour! Je suis Rubeus Hagrid, gardien des clés et des lieux à Poudlard",end="")
        input()
    elif choix == 3:
        print("*Tu vois ta porte se détacher de son cadre avec un bruit assourdissant…*",end="")
        input()
        print("Bonjour! Je suis Rubeus Hagrid, gardien des clés et des lieux à Poudlard", end="")
        input()
        porte_casse = True
    else:
        print("C'est quoi de la pizza? C'est bon? Peu importe, passons aux choses sérieuses",end="")
        input()
        print("Bonjour! Je suis Rubeus Hagrid, gardien des clés et des lieux à Poudlard", end="")
        input()
    print("Tu es un sorcier, {} {}, il est temps que tu ailles acheter tes fournitures scolaires pour la rentrée scolaire!".format(joueur["nom"],joueur["prenom"]))



