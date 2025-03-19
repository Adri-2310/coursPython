"""
__author__= "Mertens Adrien"
__version__ = "1.0"
"""


def tableau_2D_1():
    tab = [[0]*6]*13
    print(tab)


def tableau_2D():
    tab = [[0 for _ in range(8)] for _ in range(12)]

    for i in range(12):
        for j in range(8):
            tab[i][j] = i +j

    return print(max(max(row) for row in tab))


if __name__ == '__main__':
    tableau_2D()
