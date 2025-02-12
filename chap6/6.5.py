"""
__author__ = "Mertens Adrien"
__version__ = "1.0"
"""
nb_user : int = int(input("Veuillez entré un nombre: "))
print(f"Table de {nb_user}")
for i in range(1,11):
    print(f"{nb_user} X {i} = {nb_user * i}")