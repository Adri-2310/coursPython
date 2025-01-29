"""
 Écrivez un algorithme qui réponde True si un mot donné par l’utilisateur est avant le mot
 combinatoire dans le dictionnaire.

__author__ = "Mertens Adrien"
__version__ = "1.0"
"""
#assign and input
answer_user = input("Veuillez entrez un mots : ")

# check if answer_user is before combinatoire
print(f"le mot ({answer_user}) est avant le mot (combinatoire): {answer_user < "combinatoire"}")