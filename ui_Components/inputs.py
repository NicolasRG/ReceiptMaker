from tkinter import Entry, Frame


class InputBox(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        vcmd = (self.register(self.verify_input), '%P')
        self.input_box = Entry(parent, validate="key", validatecommand=vcmd)

    def verify_input(self, inp):
        if inp.isnumeric():
            return True
        print(inp + " is not a number")
        return False

    def pack(self, side=None, fill=None):
        if side is None and fill is None:
            self.input_box.pack()
        else:
            print("Has options")
