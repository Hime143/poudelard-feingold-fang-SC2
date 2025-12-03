def demander_texte(message):
    txt = input(message)
    while txt.strip() == "":
        txt = input("veuillez écrire quelque chose")
    else:
        return txt