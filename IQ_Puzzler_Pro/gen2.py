from generation import*



def write_grid(grid):  # écrit la grille dans un fichier
    f = open("grid.txt", "w")

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):
            f.write(str(grid[l][c]) + " ")
        f.write("\n")

    f.close()

def read_grid(grid):  # lit la grille dans un fichier
    f = open("grid.txt", "r")
    for l in range(NB_LINE):
        for c in range(NB_COLUMN):
            grid[l][c] = f.readline().split()

    f.close()

    return grid