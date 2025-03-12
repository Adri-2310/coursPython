"""
__author__= "Mertens Adrien"
__version__ = "1.0"
"""

def tableau1 ()->list:
    """Écrivez un algorithme qui déclare et remplisse un tableau de 7 valeurs numériques en les
    mettant toutes à 0."""
    table = [0]*7
    return table


def voyelles():
    """Écrivez un algorithme qui déclare et remplisse un tableau contenant les 6 voyelles de
    l’alphabet latin."""
    return list("aeiouy")

def notes() -> list:
    """Écrivez un algorithme qui déclare un tableau de 9 notes, dont on fait ensuite saisir les
    valeurs par l’utilisateur.
    """
    tab = [j for j in range(0,9)]
    for i in range(9):
        tab[i] = int(input(f"entré la valeurs de la note {i+1}:"))
    return tab

def notes2()->int:
    """Modifiez l’algorithme Notes afin d’effectuer et d’afficher le calcul de la moyenne des notes."""
    tab = notes()
    total : int = 0
    for i in range(0,len(tab)):
        total += tab[i]
    return total /len(tab)

if __name__ == '__main__':
    print(notes2())