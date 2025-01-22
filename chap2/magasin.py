"""Écrivez un algorithme qui lit le nom d’un article, son prix hors taxe, le nombre d’articles
et le taux de TVA, puis qui fournit le prix total TTC correspondant. Faites en sorte que
l’algorithme pose des questions claire et affiche un résultat complet."""

"""
__author__ = Adrien Mertens
__version__= 0.1.0
"""

nameItem = str(input("Le nom de l'article : "))
prixHtva = float(input("Le prix HTV : "))
quantity = int(input("Le nombre d'article : "))
tauxTVA = int(input("Le taux de TVA : "))
valeurTVA = prixHtva * quantity / 100 * tauxTVA

print(
    f"l'article : {nameItem} qui a un prix HVTA de {prixHtva}, avec une quantité de {quantity} et un taux de tva {tauxTVA}. le prix TVAC est de {prixHtva * quantity + valeurTVA}"
)
