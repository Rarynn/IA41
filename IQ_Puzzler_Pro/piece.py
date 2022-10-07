class Piece:

    def __init__(self, val, size, list):
        self.val = val
        self.size = size
        self.list = list

    def width_length_piece(self):

        # En supposant que la pièce ait un référentiel (0, 0)

        max_widt h = 0
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
