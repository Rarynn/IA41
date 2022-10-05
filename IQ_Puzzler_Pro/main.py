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


generate_button = Button(window, text="Générer", font='Helvetica 15 bold',
                         background='light gray', command=(lambda: create_grid(cnv)))

generate_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=TAB_GAP + 3 * COTE_CASE)


# grid = create_grid(cnv)

# draw_grid_colour(cnv, grid)
# show_number_grid(cnv, grid)


window.mainloop()