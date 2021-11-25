"""
Module: sudoku.py Un programme pour manipuler des grilles de sudoku.

Les variables grille_x peuvent vous servir à tester votre programme.
Elles représentent toutes des grilles de Sudoku valides à divers
stades d'avancement: grille_0 est vide, grille_1 semi-remplie et
grille_2 entièrement remplie.
"""
import time

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

grille_3 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 0],
    [7, 9, 0, 0, 0, 5, 4, 8, 0],
    [4, 8, 3, 9, 7, 1, 6, 2, 0],
    [8, 1, 4, 5, 9, 7, 2, 3, 0],
    [2, 3, 6, 1, 8, 4, 9, 5, 0],
    [0, 5, 7, 3, 2, 6, 8, 1, 0],
    [0, 0, 0, 4, 3, 2, 1, 7, 0],
    [0, 0, 0, 7, 1, 8, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
grille_4 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 1, 2, 7, 1, 8, 5, 6, 9],
    [0, 7, 8, 6, 5, 9, 3, 4, 2],
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
    return x[i-1]


def unique(x):
    tmp = set()
    for i in range(len(x)):
        if x[i] != 0:
            if x[i] not in tmp:
                tmp.add(x[i])
            else:
                return False
    return True


def colonne(x, i):
    col = []
    for j in range(len(x)):
        col.append(x[j][i-1])
    return col


def region(x, i):
    reg = []
    for j in range(1, len(x)+1):
        for h in range(1, len(x)+1):
            k = 3 * ((j - 1)//3) + ((h - 1)//3) + 1
            if k == i:
                reg.append(x[j-1][h-1])
    return reg


def ajouter(x, i, j, v):
    tmp = x[i-1][j-1]
    x[i-1][j-1] = v
    k = 3 * ((i - 1)//3) + ((j - 1)//3) + 1 #j la a place de i
    if unique(ligne(x, i)) and unique(colonne(x, j)) and unique(region(x, k)):
        # x[i-1][j-1] = v
        print("valeur correcte")
    else:
        x[i-1][j-1] = tmp
        print("l'ajout est interdit")
    

def verifier(x):
    for i in range(1, len(x)+1):
        for j in range(1, len(x)+1):
            k = 3 * ((i - 1)//3) + ((j - 1)//3) + 1    #j la a place de i
            # print(unique(ligne(x, i)))
            if unique(ligne(x, i)) and unique(colonne(x, j)) and unique(region(x, k)):       # a verif si ca marche toujours avec les and au lieu des or 
                # print(unique(ligne(x, i)))
                pass
            else:
                return False
    return True



def jouer(x):
    while verifier(x):
        i = int(input("Veuillez rentrer la ligne :"))
        j = int(input("veuillez rentrer la colonne:"))
        v = int(input("Veuillez rentrer la valeur a inserer:"))
        ajouter(x, i, j, v)
        afficher(x)
# est-ce qu'il faut faire verif a chaque fois

# jouer(grille_1)
# ajouter(grille_0, 1, 1, 1)


def solution(x):
    dico = {d: [] for d in range(10)}

    for i in range(1,len(x)+1):
        for j in range(1,len(x)+1):
            k = 3 * ((i - 1)//3) + ((j - 1)//3) + 1
            if x[i-1][j-1] == 0:     # changer ca
                tmp = []
                for y in range(1, 10):  # changer et pas mettre le 0

                    if y not in ligne(x, i) and y not in colonne(x, j) and y not in region(x, k):
                        tmp.append(y)
                         
                dico[len(tmp)].append((i, j, tmp)) 
            
    return dico

# il faut in in ou not in et exclure les valeurs deja presentes dans la ligne colonne region puis ajouter au dico sous forme de tuples 
#il fautr verif que le ligne colonne region n'est pas pleine avec la fonction unique 
# Si les trois unique retournent true alors la valeur il faut la mettre dans une list ou quelque part

# ou alors if x[i][j] in ligne colonne et region alors la tej de la list


#rajouter des comprehension de liste


def resoudre(x):
    l = [list(solution((x)).values())[i][j] for i in range(len(solution(x))) for j in range(len(solution(x)[i]))]
    if solution(x)[0]:
        return False
    if not l:
        return x
    for i in range(len(l)):
        for j in range(len(l[i][2])):
            x[l[i][0]-1][l[i][1]-1] = l[i][2][j]
            if resoudre(x):
                return True         # je pas quoi mettre ici
            else:
                x[l[i][0]-1][l[i][1]-1] = 0
        return False



        # l = [y for x in solution(grille_3).values()[x]]

# est-ce que la liste l doit etre du type l[i] renvoie une liste de tuples ou renvoie juste un tuple 
# en utilisant comphrehension de liste 
# pour les conditions d'arret 


# print(resoudre(grille_3))

l = []
# [l.append(test[z][f]) for z in range(len(test)) for f in range(len(test[z]))]
# print(l)
l = [list(solution((grille_3)).values())[i][j] for i in range(len(solution(grille_3))) for j in range(len(solution(grille_3)[i]))]


# print(resoudre(grille_3))
print(solution(grille_4)[0])

for i in l:
    pass

print(l[15][2])
print(len(l[15][2]))

resoudre(grille_0)
afficher(grille_0)
print(verifier(grille_0))
"""
for i in range(len(l)):
        for j in range(len(l[i][2])):
            print(l[i][0]-1)
            print(l[i][1]-1)
            print(l)
            time.sleep(10)
"""
