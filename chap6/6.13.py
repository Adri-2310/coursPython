"""
__author__ = "Mertens Adrien"
__version__ = "1.0
"""


# Function to calculate the factorial of a number
def factorielle(n):
    if n == 0:
        return 1
    else:
        resultat = 1
        for i in range(1, n + 1):
            resultat *= i
        return resultat


# Function to calculate the odds of winning in order and disorder
def calculer_chances(n, p):
    x = factorielle(n) // factorielle(n - p)  # In order
    y = factorielle(n) // (factorielle(p) * factorielle(n - p))  # In disorder
    return x, y


def main():
    n = int(input("Entrez le nombre de chevaux partants : "))
    p = int(input("Entrez le nombre de chevaux joués : "))

    x, y = calculer_chances(n, p)

    print(f"Dans l'ordre: une chance sur {x} de gagner")
    print(f"Dans le désordre: une chance sur {y} de gagner")


if __name__ == "__main__":
    main()
