from tkinter import Frame

class Item_Desc(Frame):
    bg = "white"
    height = "200"

    def __init__(self, master):
        Frame.__init__(self, master, bg=Item_Desc.bg, height=Item_Desc.height)
        self.pack()
