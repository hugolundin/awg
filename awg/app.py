import tkinter
import numpy

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

class ArbitraryWaveGenerator:
    def __init__(self, root=tkinter.Tk()):
        self.root = root
        self.frame = tkinter.Frame(self.root)
        self.root.wm_title('awg')
    
        self.figure = Figure(figsize=(5, 4), dpi=100)
        t = numpy.arange(0, 3, .01)
        self.figure.add_subplot(111).plot(t, 2 * numpy.sin(2 * numpy.pi * t))
        
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.canvas.mpl_connect("key_press_event", lambda event: key_press_handler(event, self.canvas, self.toolbar))

        self.frame.pack()
        self.root.tk.call('tk', 'scaling', 2.0)

    def run(self):
        self.root.mainloop()
