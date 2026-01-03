from univers.maison import *
from univers.personnage import *
from utils.input_utils import *

# Création des attributs du joueur
def initialiser():
    prenom = demander_texte("comment vous appelez vous?: \n")
    nom = demander_texte("et votre nom de famille: \n")
    return initialiser_personnage(nom,prenom,{"courage" : 0, "ambition" : 0, "loyauté": 0, "intelligence" : 0})

#Introduction à l'histoire
def introduction():
    print("Bienvenue en 1990... 10 ans depuis la disparition de Lord Voldemort.",end="")
    input()
    print("Issu d'une famille puissante de sorciers, tu atteins l'âge de tes 11 ans et tu t'apprêtes à faire ta rentrée à Poudlard.",end="")
    input()
    print("Tu attends ta lettre d'acceptation pour t'aventurer sur le Chemin de Traverse...",end="")
    input()

#invitation à Poudlard
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
#Première rencontre avec Hagrid
def coucouHagrid(joueur):
    global porte_casse
    print("Toc,toc...Tu te lèves pour aller ouvrir, tu tombes nez à nez avec un géant de plus de 2m et demi.",end="")
    input()
    choix = demander_choix("Surpris tu:",["*Tu recules de 5m*","demandes: -Bonjour, puis-je vous aider Monsieur..?","*claques la porte au nez*","dit: c'est vous le livreur de pizza? Vous êtes très en retard..."])
    if choix == 1 or choix == 2:
        print("Hagrid : Bonjour! Je suis Rubeus Hagrid, gardien des clés et des lieux à Poudlard",end="")
        input()
    elif choix == 3:
        print("*Tu vois ta porte se détacher de son cadre avec un bruit assourdissant…*",end="")
        input()
        print("Hagrid : Bonjour! Je suis Rubeus Hagrid, gardien des clés et des lieux à Poudlard", end="")
        input()
        porte_casse = True
    else:
        print("?? : C'est quoi de la pizza? C'est bon? Peu importe, passons aux choses sérieuses",end="")
        input()
        print("Hagrid : Bonjour! Je suis Rubeus Hagrid, gardien des clés et des lieux à Poudlard", end="")
        input()
    choix = demander_choix("Tu es un sorcier, {} {}, il est temps que tu ailles acheter tes fournitures scolaires pour la rentrée scolaire!".format(joueur["Nom"],joueur["Prenom"]),["Je sais que je suis un sorcier je suis issu des {} , oseriez vous me confondre avec un moldu?".format(joueur["Nom"]),"D'accord...mais je ne vais pas aller acheter mes fournitures scolaires avec un inconnu?","J'ai pas trop le temps, je dois aller arroser mes plantes, aller boire le thé et sortir avec mes chers parents","Oh, trop fun et où est-ce qu'on peut aller en trouver?"])
    if choix == 1:
        print("Hagrid : Haha bien sûr que tu n'es pas un moldu",end="")
        input()
        print("Hagrid : Allons sur le Chemin de Traverse!")
        input()
    elif choix == 2:
        print("Hagrid : Je suis le garde de chasse de Poudlard tu n'as rien à craindre", end="")
        input()
        print("Hagrid : Allons sur le Chemin de Traverse!")
        input()
    elif choix == 3:
        print("Hagrid : Ne t’inquiète pas tu auras tout le temps, les fournitures sont importantes pour ton éducation", end="")
        input()
        print("Hagrid : Allons sur le Chemin de Traverse!")
        input()
    else:
        print("Hagrid : Allons sur le Chemin de Traverse!")
        input()

#Achat des object utile pour le reste du jeu
def fourniture(joueur):
    global animal
    print("Tu te retrouves ainsi dans un bar appelé le Chaudron Baveur, Hagrid t'emmène à l’arrière du bar et soudain… \nil sort un parapluie rose de son manteau et commence à tapoter 3 fois une brique… ",end="")
    input()
    print("Tu te retrouves dès lors face à une magnifique allée regorgeant de boutiques et de sorciers faisant leurs achats.",end="")
    input()
    print("Hagrid : Bienvenue sur le Chemin de Traverse! Nous irons faire un tour à Gringotts la banque des sorciers,\npour retirer ton argent et faire tes achats indispensable",end="")
    input()
    print("Tu te retrouves alors face à un grand bâtiment blanc, à l’intérieur des goblins y travaillent.\nEn sortant du bâtiment du te retrouves avec 100 galions dans les poches",end="")
    input()
    print("Tu fais la visite de plusieurs boutiques et en regardant ta liste de fournitures scolaires tu remarques qu’il te faut obligatoirement:\nune baguette magique, une robe de sorcier et un manuel de potions",end="")
    input()
    while "baguette magique" not in joueur["Inventaire"] or "robe de sorcier" not in joueur["Inventaire"] or "manuel de potions" not in joueur["Inventaire"]:
        print()
        choix = demander_choix("Voici le catalogue des objets disponibles :",["Baguette magique - 35 galions","Robe de sorcier - 20 galions","Chaudron en étain - 15 galions","Manuel de potions - 25 galions","Plume magique - 5 galions","Livre enchanté - 30 galions","Balance de cuivre - 10 galions","Cape d'invisibilité - 100 galions"])
        if choix == 3 or choix == 5 or choix == 6 or choix == 7 or choix == 8:
            print("tu n'a pas besoin de ça",end="")
        elif choix == 1:
            if "baguette magique" in joueur["Inventaire"]:
                print("tu as déja acheté ça",end="")
            else:
                ajouter_objet(joueur,"Inventaire","baguette magique")
                modifier_argent(joueur,-35)
                print("Bravo tu viens d’acquérir une baguette magique",end="")
        elif choix == 2:
            if "robe de sorcier" in joueur["Inventaire"]:
                print("tu as déja acheté ça",end="")
            else:
                ajouter_objet(joueur,"Inventaire","robe de sorcier")
                modifier_argent(joueur,-20)
                print("Bravo tu viens d’acquérir une robe de sorcier", end="")
        elif choix == 4:
            if "manuel de potions" in joueur["Inventaire"]:
                print("tu as déja acheté ça",end="")
            else:
                ajouter_objet(joueur,"Inventaire","manuel de potions")
                modifier_argent(joueur,-25)
                print("Bravo tu viens d’acquérir un manuel de potions", end="")
    print()
    print("Tu peux dès à présent choisir ton animal de compagnie pour Poudlard",end="")

    choix = demander_choix("Tu remarques plusieurs animaux avec leur prix.",["une chouette - 20 galions","un chat - 15 galions","un rat - 10 galions ","un crapaud - 5 galions"])
    if choix == 1:
        print("Félicitations tu viens d’obtenir une chouette",end="")
        animal = "chouette"
        modifier_argent(joueur,-20)
    elif choix == 2:
        print("Félicitations tu viens d’obtenir un chat",end="")
        animal = "chat"
        modifier_argent(joueur,-15)
    elif choix == 3:
        print("Félicitations tu viens d’obtenir un rat",end="")
        animal = "rat"
        modifier_argent(joueur,-10)
    else:
        print("Félicitations tu viens d’obtenir un crapaud",end="")
        animal = "crapaud"
        modifier_argent(joueur,-5)
    print()

#Arriver à la gare et dans la voie 9 ¾
def arriver_gare():
    print("La fin des vacances d’été approchent et tu fais tes valises pour aller à la gare King’s Cross.",end="")
    input()
    print("Tu arrives à 10h40 à la gare de King's Cross",end="")
    input()
    print("Sur ton billet de train, tu vois voie 9 ¾, tu te figes, tu regardes encore une fois ton billet et c’est toujours marqué voie 9 ¾.",end="")
    input()
    print("Tu regardes tes parents et leur tend ton billet, ils sourient et te montre un mur du quai et te disent : ",end="")
    input()
    print("Regarde là-bas mon enfant, il faut foncer droit sur le mur et tu arriveras sur le quai 9 ¾.",end="")
    input()
    print("Il t’embrasse fort en souriant et te regarde faire:",end="")
    input()
    choix = demander_choix("Que fais-tu?",["Tu attrapes ton chariot avec ta valise et tu te met à courir à toute vitesse droit sur le mur","Tu serres ton chariot entre tes mains, et fonce un peu hésitant"])
    while choix == 2:
        choix = demander_choix("Tu te heurtes au mur incrédule et regarde tes parents qui rigolent et qui te disent de réessayer avec confiance.",["Tu attrapes ton chariot avec ta valise et tu te met à courir à toute vitesse droit sur le mur","Tu serres ton chariot entre tes mains, et fonce un peu hésitant"])
    print("Tu te retrouves alors sur le quai 9 ¾, avec une belle locomotive rouge à vapeur. \nTu montes à bord du Poudlard Express, tu trouves un compartiment vide pour t’y installer et y déposer tes valises dans le porte-bagages.\nLe train démarre lentement vers le Nord…")

def is_porte_casse():
    if porte_casse:
        return True
    else:
        return False

#fonction du chapitre 1 ensemble et transition entre chapitre 1 et 2
def lancer_chapitre_1(joueur):
    introduction()
    input()
    recevoir_lettre()
    coucouHagrid(joueur)
    fourniture(joueur)
    arriver_gare()
    print("Fin du Chapitre 1 ! Votre aventure commence à Poudlard...")
    afficher_personnage(joueur)
