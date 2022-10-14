from constante import *
from piece import *
from generation import *
import affichage


# list_piece représente la liste des pièces à poser du jeu

def resolve(grid, list_piece, cnv, list_cnv, window):

    print("resolution")

    # list_piece[0].rotation_piece()

    # list_cnv = []

    # Initialise affichage gamepieces

    for c in list_cnv:
        c.delete('all')
    list_cnv.clear()

    pos_list = []

    for piece in list_piece:
        pos_list.append((piece.val, create_possibility_list(grid, piece)))

    # pos_list.append(create_possibility_list(grid, list_piece[0]))

    for row in pos_list:

        val, l_case = row
        print(len(l_case))
        print(''.join([str(elem) for elem in row]))

    # print(pos_list)

    affichage.draw_list_pieces(window, list_piece, list_cnv)
    affichage.draw_grid_colour(cnv, grid)

    resolution_1(grid, pos_list, 0)

    affichage.draw_grid_colour(cnv, grid)

    """for p in list_piece:

        print(p.val, ":", p.ref)

        for i in p.list:

            print(i)"""


def create_possibility_list(grid, piece):

    possibility_list = []

    #print(piece.redundancy_in_rotation())

    for i in range(piece.redundancy_in_rotation()):

        # piece.is_a_rectangle()
        piece.rotation_piece()
        piece.piece_to_ref()

        for l in range(NB_LINE):
            for c in range(NB_COLUMN):

                case = piece.can_place(grid, (l, c))

                if case:
                    possibility_list.append(case)

    return possibility_list


# pos_list = listes de listes de coordonnées pour chaque pièces

def resolution_1(grid, pos_list, count):

    if is_full(grid):

        print("grille remplie")
        return True
    
    else:

        # On place les pièces une par une

        val, choice_list = pos_list[count]

        # choice_list = toutes les possibilités de la pièce "count"

        for coord_list in choice_list:

            # coord_list = 1 possibilité de la pièce

            if can_place_w_list(grid, coord_list):

                place_w_list(grid, coord_list, val)
                count += 1

                if resolution_1(grid, pos_list, count):
                    return True

                else:
                    count-=1
                    remove_w_list(grid, coord_list)

    return False


def place_w_list(grid, coord_list, val):

    for coord in coord_list:

        (l, c) = coord
        grid[l][c] = val


def can_place_w_list(grid, coord_list):

    for coord in coord_list:

        (l, c) = coord

        if not grid[l][c] == VIDE:
            return False

    return True


def remove_w_list(grid, coord_list):

    for coord in coord_list:

        (l, c) = coord
        grid[l][c] = VIDE