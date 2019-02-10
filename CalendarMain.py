import calendar
import datetime
from tkinter import *
from tkinter import ttk

class MainApp(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title('Calendario Universal')
        self.geometry('532x422')
        
        
        canvas = Canvas(width=532, height=422, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        canvas.create_rectangle(0,0, 532,40, width = 1)
        canvas.create_rectangle(0,40, 76,60, width = 1)
        canvas.create_rectangle(76,40, 152,60, width = 1)
        canvas.create_rectangle(152,40, 228,60, width = 1)
        canvas.create_rectangle(228,40, 304,60, width = 1)
        canvas.create_rectangle(304,40, 380,60, width = 1)
        canvas.create_rectangle(380,40, 456,60, width = 1)
        canvas.create_rectangle(456,40, 532,60, width = 1)
        canvas.create_line(0,60, 0,422, width = 1)
        canvas.create_line(76,60, 76,422, width = 1)
        canvas.create_line(152,60, 152,422, width = 1)
        canvas.create_line(228,60, 228,422, width = 1)
        canvas.create_line(304,60, 304,422, width = 1)
        canvas.create_line(380,60, 380,422, width = 1)
        canvas.create_line(456,60, 456,422, width = 1)
        canvas.create_line(532,60, 532,422, width = 1)
        canvas.create_line(0,121, 532,121, width = 1)
        canvas.create_line(0,182, 532,182, width = 1)
        canvas.create_line(0,243, 532,243, width = 1)
        canvas.create_line(0,304, 532,304, width = 1)
        canvas.create_line(0,365, 532,365, width = 1)
        canvas.create_line(0,426, 532,426, width = 1)

        
        
    def start(self):
        self.mainloop()
        
        
if __name__=='__main__':
    calc = MainApp()
    calc.start()
    