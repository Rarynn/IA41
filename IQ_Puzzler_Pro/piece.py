from constante import *

class Piece:

    def __init__(self, val, size, list):
        self.val = val
        self.size = size
        self.list = list

        # ref = coordo de la case la plus en haut à gauche de la matrice de la pièce
        # (0, 0) lorsque la piece n'est pas dans grid
        self.ref = self.mini_size_piece()

    def width_length_piece(self):

        # En supposant que la pièce ait un référentiel (0, 0)

        max_width = 0
        max_height = 0

        min_width = 0
        min_height = 0

        (last_l, last_c) = (0, 0)

        for i in self.list:

            (l, c) = i

            if l > max_height:
                max_height = l

            elif l < min_height:
                min_height = l

            if c > max_width:
                max_width = c

            elif c < min_width:
                min_width = c

        return max_height - min_width + 1, max_width - min_width + 1

    def rotation_piece(self):

        for i in range(len(self.list)):
            (l, c) = self.list[i]

            self.list[i] = (c, -l)

        for coordo in self.list:
            print(coordo)

    def mini_size_piece(self):

        min_l, min_c = (100, 100)

        for i in self.list:

            (l, c) = i

            if l < min_l:
                min_l = l

            if c < min_c:
                min_c = c

        return min_l, min_c

    def piece_to_ref(self):

        (l, c) = self.mini_size_piece()

        for i in range(len(self.list)):

            coordo = self.list[i]

            self.list[i] = coordo[0] - l, coordo[1] - c

        self.ref = self.mini_size_piece()

    def place_piece(self, grid, position):

        (ref_l, ref_c) = position
        case_list = []

        for i in range(len(self.list)):

            (l, c) = self.list[i]

            l += ref_l
            c += ref_c

            if 0 <= l < NB_LINE and 0 <= c < NB_COLUMN and grid[l][c] == VIDE:
                case_list.append((l, c))
            else:
                return False

        for coord in case_list:

            (l, c) = coord
            grid[l][c] = self.val

        return True










