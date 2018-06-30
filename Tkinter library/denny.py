import tkinter

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


root = tkinter.Tk()
app = Application(master=root)
app.mainloop()