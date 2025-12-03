def demander_texte(message):
    txt = input(message)
    while txt.strip() == "":
        txt = input(message)
    else:
        return txt