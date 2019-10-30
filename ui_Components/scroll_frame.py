from tkinter import Frame, Scrollbar, Canvas, RIGHT, LEFT, Y, X, BOTH, NW


class scrollFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bg="Green")
        frame = Frame(self)
        frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.canvas = Canvas(frame, bg='pink')
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=True)

        self.mailbox_frame = Frame(self.canvas, bg='purple')

        self.canvas_frame = self.canvas.create_window((0, 0),
                                                      window=self.mailbox_frame, anchor=NW)
        # self.mailbox_frame.pack(side = LEFT, fill = BOTH, expand = True)

        mail_scroll = Scrollbar(self.canvas, orient="vertical",
                                command=self.canvas.yview)
        mail_scroll.pack(side=RIGHT, fill=Y)

        self.canvas.config(yscrollcommand=mail_scroll.set)

        self.mailbox_frame.bind("<Configure>", self.OnFrameConfig)
        self.canvas.bind('<Configure>', self.FrameWidthAndHeight)
        self.inner_height = 1
        self.base_height = 0

    def OnFrameConfig(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def FrameWidthAndHeight(self, event):
        canvas_width = event.width
        self.base_height = event.height
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)

        if self.inner_height > self.base_height :
            self.canvas.itemconfig(self.canvas_frame, height=self.inner_height)
        else:
            self.canvas.itemconfig(self.canvas_frame, height=self.base_height)

    def set_inner_height(self, height):
        if height > self.base_height:
            self.inner_height = height
            self.canvas.itemconfig(self.canvas_frame,
                                   height=self.inner_height)

    def addItem(self, item):
        self.item.append(item)
        print("Added Item : " + str(item))

    def delteItem(self, item):
        list.remove(item)
