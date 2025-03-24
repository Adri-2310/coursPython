"""
__author__= "Adrien Mertens"
__version__ = "1.0"
"""

number_user = int(input("Veuillez entré un nombre: "))
i: int = 1

while i < 6:
    print(f"le nombre suivant par 2 est : {number_user + (i * 2)}")
    i += 1
