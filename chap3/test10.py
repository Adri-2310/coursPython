"""
 Écrivez un algorithme qui réponde True si un mot donné par l’utilisateur est après le mot
 combinatoire et avant le mot logique dans le dictionnaire.

__author__ = "Mertens Adrien"
__version__ = "1.0"
"""

# assign and input
answer_user = input("Veuillez entrez un mots : ")

# check if answer_user is before combinatoire
print(
    f"le mot ({answer_user}) est après le mot (combinatoire) et avant le mot (logique): {answer_user > 'combinatoire' and answer_user < 'logique'}"
)
