import tkinter

class ArbitraryWaveGenerator:
    def __init__(self, root=tkinter.Tk()):
        self.root = root
        self.frame = tkinter.Frame(self.root)
        self.frame.pack()

    def run(self):
        self.root.mainloop()
