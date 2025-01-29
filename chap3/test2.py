"""
 Écrivez un algorithme qui réponde True si un nombre donné par l’utilisateur est positif.
__author__= "Mertens Adrien"
__version__ = "1.0"
"""

# assign
number = int(input("Entrer un nombre entier : "))

# check if number is positive or negative
if number >= 0 :
    print(f"le nombre est positif : {number}")
else:
    print(f"le nombre est negatif : {number}")