from affichage import *
import random


TAILLE_MAX = 6
TAILLE_MIN = 3

VIDE = 0


def create_grid():

    grid = [[VIDE for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]

    count = 1

    while not is_full(grid):
        generate_piece(grid, count)
        count += 1

    return grid


def is_full(grid):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if grid[l][c] == VIDE:
                return False
    return True


def generate_piece(grid, count):

    choice_list = []

    l = random.randint(0, NB_LINE - 1)
    c = random.randint(0, NB_COLUMN - 1)

    while grid[l][c] != VIDE:
        l = random.randint(0, NB_LINE - 1)
        c = random.randint(0, NB_COLUMN - 1)

    N = size_piece()
    print(count, " --> ", N)

    grid[l][c] = count
    print(l, c)

    N -= 1

    while N > 0:

        for i in range(-1, 2, 2):

            if 0 <= l + i < NB_LINE and grid[l + i][c] == VIDE:

                if choice_list.count((l+ i, c)) == 0:
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
        print(N, ":", l2, c2)

        (l, c) = (l2, c2)

        N -= 1




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








