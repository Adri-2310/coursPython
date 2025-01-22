"""Écrivez un algorithme permettant de transférer les valeurs de trois variables a, b et c. Il
faut transférer a dans b, b dans c et c dans a, quels que soient les contenus préalables
de ces variables."""

"""
__author__ = Adrien Mertens
__version__= 0.1.0
"""

a = 1
b = 2
c = 3

print(f"a vaut {a}, b vaut {b}, c vaut {c}")

temp = c
c = b
b = a
a = temp

print(f"maintenant a vaut {a}, b vaut {b}, c vaut {c}")
