"""
__author__ = "Mertens Adrien"
__version__ = "1.0"
"""

# Assign and declare variables
price: int  # Variable to store the input price
flag_end: bool = True  # Flag to control the input loop
total_price: int = 0  # Variable to accumulate the total price

# Variables to store the count of each denomination
money_500: int = 0
money_200: int = 0
money_100: int = 0
money_50: int = 0
money_20: int = 0
money_10: int = 0
money_5: int = 0
money_2: int = 0
money_1: int = 0

# Prompt the user to enter prices
print("Veuillez entrer 0 si vous avez entré tout les prix")
while flag_end:
    price = int(input("Veuillez entrer le prix :"))  # Read the input price
    total_price += price  # Add the input price to the total price
    if price == 0:
        flag_end = False  # Exit the loop if the input is 0

# Calculate the number of each denomination needed
while total_price != 0:
    if total_price >= 500:
        money_500 = total_price // 500  # Calculate the number of 500 euro bills
        total_price %= 500  # Update the remaining total price
    elif total_price >= 200:
        money_200 = total_price // 200  # Calculate the number of 200 euro bills
        total_price %= 200  # Update the remaining total price
    elif total_price >= 100:
        money_100 = total_price // 100  # Calculate the number of 100 euro bills
        total_price %= 100  # Update the remaining total price
    elif total_price >= 50:
        money_50 = total_price // 50  # Calculate the number of 50 euro bills
        total_price %= 50  # Update the remaining total price
    elif total_price >= 20:
        money_20 = total_price // 20  # Calculate the number of 20 euro bills
        total_price %= 20  # Update the remaining total price
    elif total_price >= 10:
        money_10 = total_price // 10  # Calculate the number of 10 euro bills
        total_price %= 10  # Update the remaining total price
    elif total_price >= 5:
        money_5 = total_price // 5  # Calculate the number of 5 euro coins
        total_price %= 5  # Update the remaining total price
    elif total_price >= 2:
        money_2 = total_price // 2  # Calculate the number of 2 euro coins
        total_price %= 2  # Update the remaining total price
    elif total_price >= 1:
        money_1 = total_price // 1  # Calculate the number of 1 euro coins
        total_price %= 1  # Update the remaining total price

# Print the result
print(f"La somme totale est : {total_price} \nEt la monnaie est la suivante :"
      f"\nPièces de 1€: {money_1}"
      f"\nPièces de 2€: {money_2}"
      f"\nBillets de 5€: {money_5}"
      f"\nBillets de 10€: {money_10}"
      f"\nBillets de 20€: {money_20}"
      f"\nBillets de 50€: {money_50}"
      f"\nBillets de 100€: {money_100}"
      f"\nBillets de 200€: {money_200}"
      f"\nBillets de 500€: {money_500}")
