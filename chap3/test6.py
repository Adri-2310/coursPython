"""
Écrivez un algorithme qui réponde True si un nombre donné par l’utilisateur est divisible
 par 3.

__author__ = "Mertens Adrien"
__version__ = "1.0"
"""

#assign and input
number = int(input("Entrer un nombre entier : "))

# check if number is divisible by 3
print(f"est ce que le nombre {number} est divisible par 3. {number % 3 == 0}")