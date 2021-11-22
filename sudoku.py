"""
Module: sudoku.py Un programme pour manipuler des grilles de sudoku.

Les variables grille_x peuvent vous servir à tester votre programme.
Elles représentent toutes des grilles de Sudoku valides à divers
stades d'avancement: grille_0 est vide, grille_1 semi-remplie et
grille_2 entièrement remplie.
"""

grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

"""
Les deux fonctions ci-dessous sont données à titre d'exemple.  Le
reste est à programmer à la suite de ces fonctions.
"""


def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1, 9+1):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])


def ligne(x, i):
    if i < 1 or i > 9:
        return "Veuillez rentrer un indice compris entre 1 et 9."
    return x[i-1]


def unique(x):
    tmp = []
    for i in range(len(x)):
        if x[i] != 0:
            if x[i] not in tmp:
                tmp.append(x[i])
            else:
                return False
    return True



def colonne(x, i):
    col = []
    if i < 1 or i > 9:
        return "Veuillez rentrer un indice compris entre 1 et 9.46"
    for j in range(len(x)):
        col.append(x[j][i-1])

    return col


def region(x, i):
    reg = []
    if i < 1 or i > 9:
        return "Veuillez rentrer un indice compris entre 1 et 9."
    for j in range(1, len(x)+1):
        for h in range(1, len(x)+1):
            k = 3 * ((j - 1)//3) + ((h - 1)//3) + 1
            if k == i:
                reg.append(x[j-1][h-1])
    return reg


def ajouter(x, i, j, v):
    tmp = x[i-1][j-1]
    x[i-1][j-1] = v
    k = 3 * ((j - 1)//3) + ((i - 1)//3) + 1
    if unique(ligne(x, i)) and unique(colonne(x, j)) and unique(region(x, k)):
        # x[i-1][j-1] = v
        print("valeur correcte")
    else:
        x[i-1][j-1] = tmp
        print("l'ajout est interdit")
    



print(region(grille_2, 9))

print(unique(grille_2))
print(colonne(grille_2, 0))

ajouter(grille_1, 9, 9, 6)   # check le if indice compris entre 1 et 9
afficher(grille_1)
print(unique(ligne(grille_2, 1)))


def verifier(x):
    for i in range(1, len(x)):
        for j in range(1, len(x)):
            k = 3 * ((j - 1)//3) + ((i - 1)//3) + 1
            print(unique(ligne(x, i)))
            if unique(ligne(x, i)) or unique(colonne(x, j)) or unique(region(x, k)):
                print(unique(ligne(x, i)))
                print("bite")
            else:
                return False
    return True


print(verifier(grille_2))








