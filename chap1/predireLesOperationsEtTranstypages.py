"""Prédire les opérations et transtypages"""

# 1
print(f"Le résultat de str(4) * int('3') est : {str(4) * int('3')}")
# On répète la chaîne '4' trois fois. Cela donne '444'.

# 2
print(f"Le résultat de int('3') + float('3.2') est : {int('3') + float('3.2')}")
# On convertit '3' en entier et '3.2' en flottant, puis on additionne. Le résultat est 6.2.

# 3
print("Le résultat de str(3) * float('3.2') est : ERREUR")
# On essaie de multiplier une chaîne par un nombre flottant, ce qui génère une erreur.

# 4
print(f"Le résultat de str(3/4) * 2 est : {str(3/4) * 2}")
# On divise 3 par 4, ce qui donne 0.75, puis on le convertit en chaîne. Résultat : '0.750.75'.
