import json

def demander_texte(message):
    txt = input(message)
    while txt.strip() == "":
        txt = input(message)
    return txt

def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()

        # Vérifier si entrée vide
        if saisie == "":
            print("Veuillez entrer un nombre entre", min_val, "et", max_val, ".")
            continue

        # Gérer le signe négatif
        negatif = False
        if saisie[0] == "-":
            saisie = saisie[1:]
            if saisie == "":
                print("Veuillez entrer un nombre entre", min_val, "et", max_val, ".")
                continue
            else:
                negatif = True


        # Vérifier que tous les caractères sont des chiffres
        est_valide = True
        for c in saisie:
            if c < '0' or c > '9':
                est_valide = False
                break

        if not est_valide:
            print("Veuillez entrer un nombre valide (uniquement chiffres).")
            continue

        #convertion en int
        nombre = 0
        for c in saisie:
            nombre = nombre * 10 + (ord(c) - ord('0'))
        if negatif:
            nombre = -nombre

        # Vérifier bornes si présentes
        if min_val is not None and nombre < min_val:
            print("Veuillez entrer un nombre entre",min_val,"et",max_val,".")
            continue
        if max_val is not None and nombre > max_val:
            print("Veuillez entrer un nombre entre",min_val,"et",max_val,".")
            continue

        return nombre


def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print("{}. {}".format(i+1, options[i]))
    choix = demander_nombre("votre choix : ", 1, len(options))
    return choix

def load_fichier(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        donnees = json.load(f)
    return donnees