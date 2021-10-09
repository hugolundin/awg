import tkinter
import numpy
import inspect

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

        label = tkinter.Label(self.root, text='Function')
        text = tkinter.StringVar()
        text.trace('w', lambda name, index, mode, text=text: self.on_change(text))
        field = tkinter.Entry(self.root, textvariable=text, width=40)
        
        self.canvas.get_tk_widget().grid(row=0, columnspan=2)
        label.grid(row=1, column=0)
        field.grid(row=1, column=1)
        

        # self.figure = Figure(figsize=(5, 4), dpi=100)
        # t = numpy.arange(0, 3, .01)
        # self.figure.add_subplot(111).plot(t, 2 * numpy.sin(2 * numpy.pi * t))
        
        # self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        # self.canvas.draw()
        # self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
    def on_change(self, text):
        
        t = numpy.arange(0, 3, .01)
        
        self.figure.clear()
        self.figure.add_subplot(111).plot(t, eval(text.get()))
        self.canvas.draw_idle()

    def run(self):
        self.root.mainloop()
