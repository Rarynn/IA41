from generation import*

def read_grid(grid):  # lit la grille dans un fichier
    f = open("grid.txt", "r")
    for c in range(NB_COLUMN):
        for l in range(NB_LINE):
            grid[l][c]=f.readline().split()

    f.close()

    return grid