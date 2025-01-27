"""
Écrivez un algorithme permettant d’échanger les valeurs de deux variables a et b, et ce
quel que soit le contenu préalable.
__author__ = Adrien Mertens
__version__= 0.1.0
"""

a, b = 10, 20


print(f"a = {a} et b = {b} avant")

a, b = b, a

print(f"a = {a} et b = {b} après")
