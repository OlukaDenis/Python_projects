from tkinter import *


def frame(source, side):
    storeObject = Frame(source, borderwidth = 4, bd = 4, bg="#92a8d1")
    storeObject.pack(side=side, expand=YES, fill=BOTH)
    return storeObject

def button(source, side, text, command = None):
    storeObject = Button(source, text=text, fg="white", bg="black", command=command)
    storeObject.pack(side=side, expand=YES, fill=BOTH)

class myCalc(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add("*Font", "arial 25 bold")
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Denny Calculator")

        #displaying the number screen area
        display = StringVar()
        Entry(self, relief=FLAT, #Can also use RIDGE, RAISED, SUNKEN, GROOVE, FLAT
              textvariable = display, justify = "right", bd = 30,
              bg = "white").pack(side = TOP, expand = YES, fill = BOTH)

            #For the clear buttons
        for clearButton in (["CE"], ["C"]):
            erase = frame(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar,
                       lambda storeObject = display, q = ichar: storeObject.set(""))

        #For number buttons
        for numberButton in ("789/", "456*", "123-", "0.+"):
            numberFunction = frame(self, TOP)
            for ichar in numberButton:
                button(numberFunction, LEFT, ichar, 
                        lambda storeObject = display, q = ichar: storeObject.set(storeObject.get() + q))

        #For the equals sign
        equalsButton = frame(self, TOP)
        for ichar in "=":
            if ichar == "=":
                btnEquals = button(equalsButton, LEFT, ichar)
                btnEquals.bind("<ButtonRelease-1>",
                    lambda e, s = self, storeObject = display: s.calc(storeObject), "+")
            else:
                btnEquals = button(equalsButton, LEFT, ichar,
                    lambda storeObject = display, s = " %s "%ichar: storeObject.set(storeObject.get() +s))

    def calc(self, display):
         try:
             display.set(eval(display.get()))
         except:
             display.set("SNYNTAX ERROR")

    #def bind(self, sequence, func):
        #self.func= btnEquals

if __name__ == "__main__":
    myCalc().mainloop()
