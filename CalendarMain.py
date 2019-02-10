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

        canvas.create_text(266,20, anchor=(CENTER), font=('Arial', '24', 'bold'), text='Febrero 2019')
        canvas.create_text(38,50, anchor=(CENTER), font=('Arial', '11'), text='Lunes')
        canvas.create_text(114,50, anchor=(CENTER), font=('Arial', '11'), text='Martes')
        canvas.create_text(190,50, anchor=(CENTER), font=('Arial', '11'), text='Miércoles')
        canvas.create_text(266,50, anchor=(CENTER), font=('Arial', '11'), text='Jueves')
        canvas.create_text(342,50, anchor=(CENTER), font=('Arial', '11'), text='Viernes')
        canvas.create_text(418,50, anchor=(CENTER), font=('Arial', '11'), text='Sábado')
        canvas.create_text(494,50, anchor=(CENTER), font=('Arial', '11'), text='Domingo')

        canvas.create_text(68,113, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='28')
        canvas.create_text(144,113, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'),text='29')
        canvas.create_text(220,113, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'),text='30')
        canvas.create_text(296,113, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'),text='31')
        canvas.create_text(372,113, anchor=('se'), font=('Arial', '28', 'bold'), text='1')
        canvas.create_text(448,113, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#FF6157'),text='2')
        canvas.create_text(524,113, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#FF6157'), text='3')
        canvas.create_text(68,174, anchor=('se'), font=('Arial', '28', 'bold'), text='4')
        canvas.create_text(144,174, anchor=('se'), font=('Arial', '28', 'bold'), text='5')
        canvas.create_text(220,174, anchor=('se'), font=('Arial', '28', 'bold'), text='6')
        canvas.create_text(296,174, anchor=('se'), font=('Arial', '28', 'bold'), text='7')
        canvas.create_text(372,174, anchor=('se'), font=('Arial', '28', 'bold'), text='8')
        canvas.create_text(448,174, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#FF6157'),text='9')
        canvas.create_text(524,174, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#FF6157'), text='10')
        canvas.create_text(68,235, anchor=('se'), font=('Arial', '28', 'bold'), text='11')
        canvas.create_text(144,235, anchor=('se'), font=('Arial', '28', 'bold'), text='12')
        canvas.create_text(220,235, anchor=('se'), font=('Arial', '28', 'bold'), text='13')
        canvas.create_text(296,235, anchor=('se'), font=('Arial', '28', 'bold'), text='14')
        canvas.create_text(372,235, anchor=('se'), font=('Arial', '28', 'bold'), text='15')
        canvas.create_text(448,235, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#FF6157'),text='16')
        canvas.create_text(524,235, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#FF6157'), text='17')
        canvas.create_text(68,296, anchor=('se'), font=('Arial', '28', 'bold'), text='18')
        canvas.create_text(144,296, anchor=('se'), font=('Arial', '28', 'bold'), text='19')
        canvas.create_text(220,296, anchor=('se'), font=('Arial', '28', 'bold'), text='20')
        canvas.create_text(296,296, anchor=('se'), font=('Arial', '28', 'bold'), text='21')
        canvas.create_text(372,296, anchor=('se'), font=('Arial', '28', 'bold'), text='22')
        canvas.create_text(448,296, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#FF6157'), text='23')
        canvas.create_text(524,296, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#FF6157'), text='24')
        canvas.create_text(68,357, anchor=('se'), font=('Arial', '28', 'bold'), text='25')
        canvas.create_text(144,357, anchor=('se'), font=('Arial', '28', 'bold'), text='26')
        canvas.create_text(220,357, anchor=('se'), font=('Arial', '28', 'bold'), text='27')
        canvas.create_text(296,357, anchor=('se'), font=('Arial', '28', 'bold'), text='28')
        canvas.create_text(372,357, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='1')
        canvas.create_text(448,357, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='2')
        canvas.create_text(524,357, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='3')
        canvas.create_text(68,418, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='4')
        canvas.create_text(144,418, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='5')
        canvas.create_text(220,418, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='6')
        canvas.create_text(296,418, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='7')
        canvas.create_text(372,418, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='8')
        canvas.create_text(448,418, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='9')
        canvas.create_text(524,418, anchor=('se'), font=('Arial', '28', 'bold'), fill=('#c2c2c2'), text='10')

        
        
    def start(self):
        self.mainloop()
        
        
if __name__=='__main__':
    calc = MainApp()
    calc.start()
    