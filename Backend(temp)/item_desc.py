from tkinter import Frame, X, Y, Button
from inputs import InputBox

ITEM_HEIGHT = .09
ITEM_WIDTH = .970
PADDINGX = .005
PADDINGY = .01
BG = "Grey"

class Item_Desc(Frame):

    def __init__(self, master, item, removeItem):
        Frame.__init__(self, master, bg=BG, height=75)
        self.item = item
        self.removeItem = removeItem
        #add in inputs
        self.delete_button = Button(self, text="X", command=self.deleteMe)
        self.name = InputBox(self, type="Word")
        self.quantity = InputBox(self)
        self.price = InputBox(self)
        #place entry boxs
        self.delete_button.place(relx=.001, rely=.05, relwidth=.10, relheight=.90)
        self.name.place(relx=.105, rely=.05, relwidth=.47, relheight=.90)
        self.quantity.place(relx=.63, rely=.05, relwidth=.20, relheight=.9)
        self.price.place(relx=.84, rely=.05, relwidth=.1599, relheight=.9)
        #register event listeners, might just change these to add to item instead or 
        # recall get on the total button 
        self.name.bind("<FocusOut>", self.onExitName)
        self.quantity.bind("<FocusOut>", self.onExitQuantity)
        self.price.bind("<FocusOut>", self.onExitPrice)
        

    def onExitName(self, e):
        print(self.getName())
        self.item.set_name(self.getName())

    def onExitQuantity(self, e):
        print(self.getQauntity())
        self.item.set_amount(self.getQauntity())

    def onExitPrice(self, e):
        print(self.getPrice())
        self.item.set_price(self.getPrice())

    def addToView(self):
        self.pack(fill=X)

    def getName(self):
        return self.name.input_box.get()

    def getQauntity(self):
        return self.quantity.input_box.get()

    def fill(self):
        self.name.setStringVar(self.item.get_name())
        self.price.setStringVar(self.item.get_price())
        self.quantity.setStringVar(self.item.get_amount()) 

    def getPrice(self):
        return self.price.input_box.get()
    
    def deleteMe(self):
        self.removeItem(self.item)
        print("delte me" + str(self))