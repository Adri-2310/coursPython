"""
Écrivez un algorithme qui lit le nom d’un article, son prix hors taxe, le nombre d’articles
et le taux de TVA, puis qui fournit le prix total TTC correspondant. Faites en sorte que
l’algorithme pose des questions claires et affiche un résultat complet.

__author__ = "Adrien Mertens"
__version__ = "0.1.0"
"""

# Assignation et affectation
nameItem = str(input("Le nom de l'article : "))
prixHtva = float(input("Le prix HTVA (le prix sans le signe euro €) : "))
quantity = int(input("Le nombre d'articles (en un chiffre entier) : "))
tauxTVA = int(
    input(
        "Le taux de TVA (sans le % et le nombre entier uniquement donc 21 pour 21%) : "
    )
)

# Calculer la somme totale de TVA
valeurTVA = (prixHtva * quantity * tauxTVA) / 100

# Afficher le résultat complet avec toutes les données
print(
    f"L'article : {nameItem} qui a un prix HTVA de {prixHtva} €, avec une quantité de {quantity} et un taux de TVA de {tauxTVA}%. Le prix TVAC est de {(prixHtva * quantity) + valeurTVA} €."
)
