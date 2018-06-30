
from tkinter import *
root = Tk()
label1=Label(root, text="Name")
label2=Label(root, text="Password")
entry1=Entry(root, width="30")

entry2=Entry(root, width="30")
label1.grid(row=0)
label2.grid(row=1)


entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry2.config(show="*")
check1=Checkbutton(root,text="Keep me logged in")
check1.grid(columnspan=2)
root.mainloop()
