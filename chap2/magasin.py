"""
__author__ = "Adrien Mertens"
__version__ = "0.1.0"

"""

# Assignment and input
nameItem = str(input("The name of the item: "))
priceExclTax = float(input("The price excluding tax (without the euro sign €): "))
quantity = int(input("The number of items (as an integer): "))
vatRate = int(input("The VAT rate (as an integer, e.g., 21 for 21%): "))

# Calculate the total VAT amount
vatAmount = (priceExclTax * quantity * vatRate) / 100

# Display the complete result with all data
print(
    f"The item: {nameItem} with a price excluding tax of {priceExclTax} €, with a quantity of {quantity} and a VAT rate of {vatRate}%. The total price including tax is {(priceExclTax * quantity) + vatAmount} €."
)
