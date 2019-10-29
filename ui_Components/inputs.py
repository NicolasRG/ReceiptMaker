from tkinter import Entry, Frame


class InputBox(Frame):

    def __init__(self, parent, type="Number"):
        Frame.__init__(self, parent, bg="black")

        self.type = type

        vcmd = (self.register(self.verify_input), '%P')
        self.input_box = Entry(self, validate="key", validatecommand=vcmd)
        self.input_box.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)

    def verify_input(self, inp):
        if self.type == "Word":
            return True
        if inp.isnumeric():
            return True
        print(inp + " is not a number")
        return False

    '''def pack(self, side=None, fill=None):
        if side is None and fill is None:
            self.input_box.pack()
        else:
            print("Has options")'''
