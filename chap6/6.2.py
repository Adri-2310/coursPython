"""
__author__ = "Mertens Adrien"
__version__= "0.1"
"""
answer : int = 0
while answer < 10 or answer > 20:
    answer=int(input("Veuillez entrer un nombre entre 10 et 20: "))
    if answer<10 or answer>20:
        if answer<10:
            print("Plus grand!")
        else:
            print("Plus petit!")

print(f"le nombre est: {answer}")