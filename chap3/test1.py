"""

 Écrivez un algorithme qui réponde True si un nombre donné par l’utilisateur est pair.

__author__= "Mertens Adrien"
__version__ = "1.0"

"""

# assign and typ
number : int = int(input("Veuillez entrez un nombre entier : "))

# check if number is pair or impair
if number % 2 == 0:
    print(f"Le nombre donné ({number}) est pair")
else:
    print(f"Le nombre donné ({number}) est impair")