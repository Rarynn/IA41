
from affichage import *
from generation import *
from resolution import *


window = Tk()
window.title("IQ Puzzler Pro")
window.geometry("1080x720")

cnv_game = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='light gray')

cnv_game.pack()
cnv_game.place(x=TAB_GAP, y=TAB_GAP)

# cnv_piece = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='light gray')

# cnv_piece.pack()
# cnv_piece.place(x=TAB_GAP, y=1 * TAB_GAP + HEIGHT_TAB)



draw_grid(cnv_game)

grid = [[0 for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]
list_game_piece = []
list_cnv = []

generate_button = Button(window, text="Générer", font='Helvetica 15 bold',
                         background='light gray', command=(lambda: create_grid(grid, list_game_piece, cnv_game, window, list_cnv)))

generate_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=TAB_GAP + 3 * COTE_CASE)

verify_button = Button(window, text="Verifier", font='Helvetica 15 bold',
                         background='light gray', command=(lambda: resolve(grid, list_game_piece, cnv_game, window)))

verify_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=TAB_GAP + 4 * COTE_CASE)

window.mainloop()
