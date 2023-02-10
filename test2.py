try:
    import Tkinter as tk     ## Python 2.x
except ImportError:
    import tkinter as tk     ## Python 3.x

class OpenToplevels():
    """ open and close Frames
    """
    def __init__(self, root):
        self.button_ctr=0
        self.root=root
        tk.Button(self.root, text="Exit Tkinter", bg="red",
                  command=self.root.quit).grid(row=10, column=2, 
                          sticky="we", rowspan=3)

        ## 3 instances ot the same class to save coding
        self.instances=[]
        for num in range(3):
            self.instances.append(AnotherTop(self.root, num+1))
            self.instances[-1].start_it()

class AnotherTop():
    def __init__(self, root, number):
        self.number=number
        ##self.top=tk.Toplevel(root)
        ##self.top.title("Toplevel #%d" % (number))
        self.fr=tk.Frame(root)
        tk.Button(self.fr, text="Close Frame #%d" % (number),
                  command=(self.close_it), bg="orange", 
                  width=20).grid(row=1, column=0)

    def close_it(self):
        self.fr.grid_forget()

    def start_it(self):
        self.fr.grid(row=self.number, column=self.number)

root = tk.Tk()
Ot=OpenToplevels(root)
root.mainloop()