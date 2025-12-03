def initialiser_personnage(nom, prenom, attributs):
    return {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs
    }

def afficher_personnage(joueur):
    print("Profil du personnage:")
    print("Nom :", joueur["Nom"])
    print("Prenom :", joueur["Prenom"])
    print("Argent :", joueur["Argent"])
    print("Inventaire :", ", ".join(joueur["Inventaire"]))
    print("Sortilèges :", ", ".join(joueur["Sortilèges"]))
    print("Attributs :")
    for cle in joueur["Attributs"]:
        print("-", cle, ":", joueur["Attributs"][cle])

def modifier_argent(joueur, montant):
    joueur["Argent"] += montant
