"""1.1 Prédire les opérations"""

# 1
print(f"Le résultat pour (1+2)**3 est : {(1+2)**3}")  # On additionne 1 + 2, ce qui donne 3, puis on élève 3 au cube.

# 2
print(f"Le résultat pour 'Da'*4 est : {'Da'*4}")  # On répète 'Da' 4 fois.

# 3
print(f"Le résultat pour 'Da'+4 est : ERREUR, mais si on transforme l'entier (4) en chaîne, cela fonctionne : {'Da'+str(4)}")
# On obtient une erreur si on essaie d'ajouter une chaîne et un entier non converti.

# 4
print(f"Le résultat de ('Pa'+'La')*2 est : {('Pa'+'La')*2}")  # On concatène 'Pa' et 'La', ce qui donne 'PaLa', puis on le répète 2 fois.

# 5
print("Le résultat de ('Da' * 4) / 2 est : ERREUR")
# On ne peut pas diviser une chaîne de caractères.

# 6
print(f"Le résultat de 5/2 est : {5/2}")  # On divise 5 par 2, ce qui donne une division avec un résultat flottant.

# 7
print(f"Le résultat de 5//2 est : {5//2}")  # On divise 5 par 2, mais on récupère uniquement la partie entière du résultat.

# 8
print(f"Le résultat de 5 % 2 est : {5%2}")  # On calcule le reste de la division de 5 par 2 (modulo).
