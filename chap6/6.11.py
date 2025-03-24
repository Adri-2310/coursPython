"""
__author__ = "Mertens Adrien"
__version__ = "1.0"
"""


def is_bisextil(year):
    """Check if a year is a leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year, month):
    """Return the number of days in the given month"""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 8, 10, 12):
        return 30
    elif month == 2:
        return 29 if is_bisextil(year) else 28
    return 0


def decal_date():
    """Shift the date according to the number of days requested"""
    # Demander à l'utilisateur d'entrer une date
    day = int(input("jour: "))
    month = int(input("mois: "))
    year = int(input("année: "))

    # Ask the user for the number of days to shift
    day_decal = int(input("Le nombre de jour a décalée : "))

    # Calculate the new shifted date
    for i in range(day_decal):
        day += 1
        if day > days_in_month(year, month):
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1

    # Display the new date
    print(f"la nouvelle date sera : {day}/{month}/{year}")


# Start algorithm
decal_date()
