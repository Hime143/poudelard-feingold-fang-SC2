def demander_texte(message):
    txt = input(message)
    while txt.strip() == "":
        txt = input(message)
    else:
        return txt

def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()

        # Vérifier si entrée vide
        if not saisie:
            print("Veuillez entrer un nombre entre",min_val,"et",max_val,".")
            continue

        # Gérer le signe négatif
        negatif = False
        if saisie[0] == "-":
            negatif = True
            saisie = saisie[1:]
            if not saisie:
                print("Veuillez entrer un nombre entre",min_val,"et",max_val,".")
                continue

        # Convertir la chaîne en entier manuellement
        nombre = 0
        est_valide = True
        for c in saisie:
            if c < min_val or c > max_val:
                est_valide = False
                break
            nombre = nombre * 10 + (ord(c) - ord("0"))

        if not est_valide:
            print("Veuillez entrer un nombre entre",min_val,"et",max_val,".")
            continue

        if negatif:
            nombre = -nombre

        # Vérifier bornes si présentes
        if min_val is not None and nombre < min_val:
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            continue
        if max_val is not None and nombre > max_val:
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            continue

        return nombre


def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print("{}. {}".format(i+1, options[i]))
    choix = demander_nombre("votre choix : ", 1, len(options))
    return choix