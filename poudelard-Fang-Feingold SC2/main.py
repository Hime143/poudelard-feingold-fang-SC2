from chapitres.chapitre_1 import *
from newfile import *
from univers.maison import *
from univers.personnage import *
from utils.input_utils import *
prenom = demander_texte("comment vous appelez vous?")
nom = demander_texte("et votre nom de famille")
introduction()
recevoir_lettre()
joueur = initialiser_personnage(prenom,nom,{"Gryffondor" : 0, "Serpentard" : 0, "Poufsouffle": 0, "Serdaigle" : 0})
coucouHagrid()