from tkinter import *
from constante import *
from affichage import *
from generation import *


window = Tk()
window.title("IQ Puzzler Pro")
window.geometry("1080x720")

cnv = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='light gray')

cnv.pack()
cnv.place(x=TAB_GAP, y=TAB_GAP)

draw_grid(cnv)

grid = [[VIDE for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]

list_piece = []

generate_button = Button(window, text="Générer", font='Helvetica 15 bold',
                         background='light gray', command=(lambda: create_grid(grid, list_piece, cnv)))

generate_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=TAB_GAP + 3 * COTE_CASE)

verify_button = Button(window, text="Verifier", font='Helvetica 15 bold',
                         background='light gray', command=(lambda: print(list_piece)))

verify_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=TAB_GAP + 4 * COTE_CASE)

window.mainloop()
