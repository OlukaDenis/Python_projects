from tkinter import *
root = Tk()
def printName(event):
    print("Hello, my name is Denis! How can I help you")

button1 = Button(root, text="Click me")

button1.bind("<Button-1>", printName)
button1.pack()


root.mainloop()
