from tkinter import *
from tkinter import ttk

class Mine():
    def __init__(self, master):
        self.whole_frame = ttk.Frame(master)
        self.whole_frame.pack()

       
        ttk.Label(self.whole_frame, text = "Username:").grid(row=0, column=0,pady=20)
        ttk.Entry(self.whole_frame, width = 20).grid(row=0, column=1,pady=20,padx=20)
        ttk.Label(self.whole_frame, text = "Password:").grid(row=1, column=0)
        pass_entry=ttk.Entry(self.whole_frame, width = 20).grid(row=1, column=1)

        button1=ttk.Button(self.whole_frame, text = "LOGIN").grid(row=3, column=0,
                                                         columnspan=2,padx=20, pady=20)
        style = ttk.Style()
        style.theme_use("vista")#changes the style of buttons and text entries
        #style.configure("TButton", foreground = "green")

        #customizing a user style
        style.configure("Denis.TButton", foreground="white",
                        background="blue", font=("Arial", 18, "bold"))
        style.map("TButton", background=[("pressed","black")],
                  foreground=[("pressed", "white"), ("disabled","grey")])
        #button1.state(["disabled"])
        button1.state(["readonly"])
        
        
        

root = Tk()
my = Mine(root)
root.mainloop()
