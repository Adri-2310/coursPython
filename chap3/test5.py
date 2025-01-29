"""
 Écrivez un algorithme qui réponde True si un nombre donné par l’utilisateur est entre 10
 et 100.
__author__ = "Mertens Adrien"
__version__ = "1.0"
"""

# assign and input
number = int(input("Entrer un nombre entre 10 et 100: "))

# check if number is in 10 and 100
print(f"est ce que le nombre est entre 10 et 100: {number>10 and number<100}")