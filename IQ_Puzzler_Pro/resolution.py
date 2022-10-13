from constante import *
from piece import *
import affichage


def resolve(grid, list_piece, cnv, list_cnv, window):

    print("resolution")

    # list_piece[0].rotation_piece()

    # list_cnv = []

    for c in list_cnv:
        c.delete('all')
    list_cnv.clear()

    for l in range(NB_LINE):
        find = False
        for c in range(NB_COLUMN):

            if list_piece[0].place_piece(grid, (l, c)):
                find = True
                break

        if find:
            break

    affichage.draw_list_pieces(window, list_piece, list_cnv)
    affichage.draw_grid_colour(cnv, grid)

    for p in list_piece:

        print(p.val, ":", p.ref)

        for i in p.list:

            print(i)
