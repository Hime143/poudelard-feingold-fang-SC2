def demander_texte(message):
    txt = input(message)
    while txt.strip() == "":
        txt = input("veuillez écrire quelque chose")
    else:
        return txt

def demander_nombre(message, min_Val = None, max_Val = None):
    nombre = input(message)
    while nombre.strip() == "":
        nombre = input("Veuillez entrez un nombre valide")
    else:
        return nombre