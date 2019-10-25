from tkinter import Tk, Label, Button, LEFT, Frame, X, Y, BOTTOM, BOTH
from inputs import InputBox
from data_format import informationStruct

class GUI:

    def __init__(self, master):
        HEADER_COLOR = "Black"
        CONTENTS_COLOR = "Grey"

        self.master = master
        master.title("A Simple App")

        # main two frames
        self.header = Frame(master, bg=HEADER_COLOR)
        self.config_header()

        self.contents = Frame(master, bg=CONTENTS_COLOR)
        self.config_contents()

        # add children to content frame
        # start with the title contents
        ITEM_TITLE_COLOR = "#4a4a4a"
        self.item_title = Frame(self.contents, bg=ITEM_TITLE_COLOR)
        self.config_item_title()

        # add frame that can be dynamic :)



    def config_header(self):
        TITLE = "One Ant Farm"
        BACKGROUND = "Black"
        WIDTH = .99
        HEIGHT = .09
        FOREGROUND = "white"
        FONT = "Arial"
        FONT_SIZE = 24
        PADDING = .005

        self.header.place(relx=PADDING, rely=PADDING, relheight=HEIGHT, relwidth=WIDTH)

        ui_title = Label(self.header, text=TITLE, fg=FOREGROUND, bg=BACKGROUND, font=(FONT, FONT_SIZE))
        ui_title.place(rely=.25, relwidth=.99)

    def config_contents(self):
        WIDTH = .99
        HEIGHT = .85
        PADDINGX = .005
        PADDINGY = PADDINGX + .1

        self.contents.place(relx=PADDINGX, rely=PADDINGY, relheight=HEIGHT, relwidth=WIDTH)

    def config_item_title(self):
        WIDTH = .99
        HEIGHT = .07
        PADDINGX = .005
        PADDINGY = .005



        self.item_title.place(relx=PADDINGX, rely=PADDINGY, relheight=HEIGHT, relwidth=WIDTH)
        #add the confugiration for the title

        ITEM_PADDINGX = .005
        ITEM_PADDINGY = .05
        ITEM_HEIGHT = .9
        LARGE_WIDTH  = .60
        SMALL_WIDTH = .19
        TEXT = "Item No/ Item Name"

        item_name = Label(self.item_title, text=TEXT)
        item_name.place(rely=ITEM_PADDINGY, relx=ITEM_PADDINGX, relwidth=LARGE_WIDTH, relheight=ITEM_HEIGHT)

        item_quantity = Label(self.item_title, text="Quantity")
        item_quantity.place(rely=ITEM_PADDINGY, relx=ITEM_PADDINGX+.605 , relwidth=SMALL_WIDTH, relheight=ITEM_HEIGHT)

        item_cost = Label(self.item_title, text="Cost")
        item_cost.place(rely=ITEM_PADDINGY, relx=ITEM_PADDINGX+.605+SMALL_WIDTH+ITEM_PADDINGX, relwidth=SMALL_WIDTH, relheight=ITEM_HEIGHT)





root = Tk()
root.geometry("1000x1000")
gui = GUI(root)
root.mainloop()
