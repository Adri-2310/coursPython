def positifOrNegatif():
    """
     Écrivez un algorithme qui demande un nombre à l’utilisateur, puis qui l’informe si ce
     nombre est positif ou négatif. On considère que 0 est positif.

    __author__ = "Mertens Adrien"
    __version__ = "1.0"
    """

    # assign and input
    number = int(input("Veuillez entrez un nombre entier: "))

    # check if number is positif or negative
    if number >= 0:
        print(f"{number} est positif.")
    else:
        print(f"{number} est negatif.")
