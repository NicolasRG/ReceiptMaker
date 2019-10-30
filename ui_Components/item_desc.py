from tkinter import Frame, X, Y
from inputs import InputBox

ITEM_HEIGHT = .09
ITEM_WIDTH = .970
PADDINGX = .005
PADDINGY = .01
BG = "Grey"

class Item_Desc(Frame):

    def __init__(self, master, item):
        Frame.__init__(self, master, bg=BG, height=75)
        self.item = item
        #add in inputs
        self.name = InputBox(self, type="Word")
        self.quantity = InputBox(self)
        self.price = InputBox(self)
        #place entry boxs
        self.name.place(relx=.001, rely=.05, relwidth=.62, relheight=.90)
        self.quantity.place(relx=.63, rely=.05, relwidth=.20, relheight=.9)
        self.price.place(relx=.84, rely=.05, relwidth=.1599, relheight=.9)



    def addToView(self):
        self.pack(fill=X)

    def getName(self):
        return self.name.input_box.get()