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

grid = create_grid(cnv)

draw_grid_colour(cnv, grid)
# show_number_grid(cnv, grid)


window.mainloop()