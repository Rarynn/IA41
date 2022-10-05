from affichage import *
import random
from piece import *


TAILLE_MAX = 6
TAILLE_MIN = 3

VIDE = 0


def create_grid(cnv):  # fonction dans laquelle nous remplissons la grille

    # Initialisation de la grille avec que des cases vides = 0
    grid = [[VIDE for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]

    # count permet de donner une valeur à chaque type de pièces
    count = 1

    # liste contenant toutes les pièces de classe pièce avec valeur, taille et liste de coordonnées
    list_piece = []

    # boucle dans laquelle nos pièces vont être créé, on retourne dans la boucle pour chaque nouvelles pièces
    while not is_full(grid):

        # créer une pièce, la positionne dans la grille et retourne la liste de coordo
        list_coordo = generate_piece(grid, count)

        # ajoute le nouvelle pièce dans liste_piece
        list_piece.append(piece(count, len(list_coordo), list_coordo))

        count += 1

    # draw_grid_colour(cnv, grid)

    for i in list_piece:
        print(i.val, "size", i.size, ":", i.list)

    # fonction qui permet de fusionner les pièces trop petites
    fusion(list_piece, grid)

    for i in list_piece:
        print(i.val, "size", i.size, ":", i.list)

    return grid


def fusion(list_piece, grid):

    for piece in list_piece:

        choice_list = []

        print(piece.val)

        if piece.size == 1:

            (l, c) = piece.list[0]
            print(piece.val)

            for i in range(-1, 2, 2):  # Parcours les cases adjacentes

                if 0 <= l + i < NB_LINE:

                    for p2 in list_piece:

                        if grid[l + i][c] == p2.val:

                            print(p2.val)
                            choice_list.append(p2)

                if 0 <= c + i < NB_COLUMN:

                    for p2 in list_piece:

                        if grid[l][c + i] == p2.val:
                            print(p2.val)
                            choice_list.append(p2)

            s_max = 10
            choosed_piece = None

            for ch in choice_list:   # choisit la pièce avec le moins de case

                p2 = ch

                if p2.size < s_max:
                    s_max = p2.size
                    choosed_piece = p2

            grid[l][c] = choosed_piece.val
            # list_piece.remove(piece)

            choosed_piece.size += 1
            choosed_piece.list.append((l, c))









def is_full(grid):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if grid[l][c] == VIDE:
                return False
    return True


def generate_piece(grid, count):

    choice_list = []
    choosed_list = []

    l = random.randint(0, NB_LINE - 1)
    c = random.randint(0, NB_COLUMN - 1)

    while grid[l][c] != VIDE:
        l = random.randint(0, NB_LINE - 1)
        c = random.randint(0, NB_COLUMN - 1)

    N = size_piece()
    print(count, " --> ", N)

    grid[l][c] = count
    choosed_list.append((l, c))
    print(l, c)

    N -= 1

    while N > 0:

        for i in range(-1, 2, 2):

            if 0 <= l + i < NB_LINE and grid[l + i][c] == VIDE:

                if choice_list.count((l + i, c)) == 0:
                    choice_list.append((l + i, c))

            if 0 <= c + i < NB_COLUMN and grid[l][c + i] == VIDE:

                if choice_list.count((l, c + i)) == 0:
                    choice_list.append((l, c + i))

        if len(choice_list) < 1:
            break

        rand = random.randint(0, len(choice_list) - 1)

        (l2, c2) = choice_list[rand]

        choice_list.remove((l2, c2))

        grid[l2][c2] = count

        choosed_list.append((l2, c2))
        print(N, ":", l2, c2)

        (l, c) = (l2, c2)

        N -= 1

    return choosed_list




def size_piece():
    r = random.randint(1, 10)

    if r <= 4:
        N = 5

    elif r <= 7:
        N = 4

    elif random.randint(1, 2) == 1:
        N = 3

    else:
        N = 6

    return N








