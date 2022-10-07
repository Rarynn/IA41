from constante import *
from piece import *
import affichage


def resolve(grid, list_piece, cnv, window):

    print("resolution")

    list_piece[0].rotation_piece()

    list_cnv = []

    affichage.draw_list_pieces(window, list_piece, list_cnv)
