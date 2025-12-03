def demander_texte(message):
    txt = input(message)
    while txt.strip() == "":
        txt = input(message)
    else:
        return txt

def demander_nombre(message, min_Val = None, max_Val = None):
    nombre = input(message)
    while nombre.strip() == "":
        nombre = input("Veuillez entrez un nombre valide")
    else:
        return nombre

def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print("{}. {}".format(i+1, options[i]))
    choix = demander_nombre("votre choix : ", 1, len(options))
    return choix