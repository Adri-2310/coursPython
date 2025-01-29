"""
 Écrivez un algorithme qui réponde True si un nombre donné par l’utilisateur est pair et
 divisible par 5.

__author__ = "Mertens Adrien"
__version__ = "1.0"
"""

# assign and input
number = int(input("Veuillez un nombre entier : "))

# check is number is impair or divisible by 5
print(
    f"est ce que le nombre ({number}) est pair et divisible par 5 ? {number % 5 == 0 and number % 2 == 0}"
)
