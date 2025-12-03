maisons = {
    "Gryffondor": 0,
    "Serpentard": 0,
    "Poufsouffle": 0,
    "Serdaigle": 0
    }

def actualiser_points_maison(maisons, nom_maison, points):
    maisons[nom_maison] += points

def  afficher_maison_gagnante(maisons):
    max =  0
    for score in maisons.values():
        if score > max:
            max = score
    gagnants = []
    for nom in maisons.keys():
        if maisons[nom] == max :
            gagnants.append(nom)
    for i in gagnants:
        print(i,end=" ")

def repartition_maison(joueur, questions):
    repartition = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
