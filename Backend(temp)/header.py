from tkinter import Frame, Label


class Header(Frame):
    text = "One Ant Farm"
    bg = "Black"
    height = "100"
    foreground = "white"
    font = "Arial"
    font_size = 48

    def __init__(self, master):
        Frame.__init__(self, master, bg=Header.bg, height=Header.height)
        self.label = Label(self, text=Header.text, bg=Header.bg, fg=Header.foreground, height=2,
                           font=(Header.font, Header.font_size))
        self.label.pack()



