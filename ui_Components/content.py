from tkinter import Frame
from item_desc import Item_Desc

class Content(Frame):
    background = "Grey"
    height = 1000

    def __init__(self, master):
        Frame.__init__(self, master, bg=Content.background, height=Content.height)

        self.item_desc = Item_Desc(self)


