from tkinter import Frame
from inputs import InputBox

ITEM_HEIGHT = .09
ITEM_WIDTH = .970
PADDINGX = .005
PADDINGY = .01
BG = "Grey"

class Item_Desc(Frame):

    def __init__(self, master, item):
        Frame.__init__(self, master, bg=BG)
        self.item = item
        #add in inputs
        self.name = InputBox(self, type="Word")
        self.quantity = InputBox(self)
        self.price = InputBox(self)
        # need to attach even handlers as well:/

        self.name.place(relx=.001, rely=.05, relwidth=.64, relheight=.90)




    def addToView(self, rely):
        self.place(relx=PADDINGX, rely=rely, relheight=ITEM_HEIGHT, relwidth=ITEM_WIDTH)
