from importlib.metadata import pass_none


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

def productPositifOrNegatif():
    """
    Écrivez un algorithme qui demande deux nombres à l’utilisateur, puis qui l’informe si leur
    produit est positif ou négatif. On laisse de côté le cas où le produit est nul. Attention,
    il ne faut pas calculer le produit!!

    __author__ = "Mertens Adrien"
    __version__ = "1.0"
    """
    # assign and input
    number_1 = int(input("Veuillez entrez un nombre entier: "))
    number_2 = int(input("Veuillez entrez un nombre entier: "))

    # check if the product de numbers is positif or negative



if __name__ == '__main__':
    productPositifOrNegatif()