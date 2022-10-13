from constante import *
from piece import *
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

    """for l in range(NB_LINE):
        find = False
        for c in range(NB_COLUMN):

            if list_piece[0].place_piece(grid, (l, c)):
                find = True
                break

        if find:
            break"""


    pos_list = []

    for piece in list_piece:
       pos_list.append(create_possibility_list(grid, piece))

    # pos_list.append(create_possibility_list(grid, list_piece[0]))


    for row in pos_list:
        print(len(row))
        print(''.join([str(elem) for elem in row]))

    # print(pos_list)

    affichage.draw_list_pieces(window, list_piece, list_cnv)
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




