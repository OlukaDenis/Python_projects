from tkinter import *
from tkinter import ttk

class Feedback:
    def __init__(self, master):
        self.frame_header = ttk.Frame(master)#creates a frame
        self.frame_header.pack()#places the frames on top
        self.logo = PhotoImage(file = "deno.png")
        ttk.Label(self.frame_header,  image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = "Thanks for visiting our site!").grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 400, text = "Hope you will enjoy your survey").grid(row = 1, column = 1)


        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        style = ttk.Style()
        ttk.Label(self.frame_content, text = "Name:").grid(row = 0, column = 0 , sticky = "sw", padx = 10)
        ttk.Label(self.frame_content, text = "Email:").grid(row = 0, column = 1 , sticky = "sw", padx = 10)
        ttk.Label(self.frame_content, text = "Comments:").grid(row = 2, column = 0 , sticky = "sw", padx = 10,  pady = 10)

        

        self.entry_name = ttk.Entry(self.frame_content, width = 24)
        self.entry_email = ttk.Entry(self.frame_content, width = 24)
        self.text_comments = Text(self.frame_content, width = 50, height = 10)

        self.entry_name.grid(row = 1, column = 0, sticky = "sw",  padx = 10)
        self.entry_email.grid(row = 1, column = 1, sticky = "sw",  padx = 10)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2,  padx = 10)
        
        ttk.Button(self.frame_content, text = "Submit").grid(row = 4, column = 0, padx = 10, sticky = "e",   pady = 10)
        ttk.Button(self.frame_content, text = "Reset").grid(row = 4, column = 1, padx = 10, stick = "w",  pady = 10)



def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__":
    main()