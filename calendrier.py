"""

__author__ = "Mertens Adrien"
__version__ = "1.0"

"""

# assign and input
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

flag = False

#
if month != 2:  # retire le mois de février
    if month in (1, 3, 5, 7, 8, 10, 12):  # on choisi les mois de 31 jours
        if day < 31:  # on prend tout les nombres au dessus de 30
            pass
        else:
            pass
    else:
        pass
else:  # le mois de février
    pass


if flag:
    print(f"le lendemain sera {day}/{month}/{year}")
