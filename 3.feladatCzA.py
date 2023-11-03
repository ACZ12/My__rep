from tkinter import *
from random import *
window=Tk()
canvas=Canvas(window,height=400,width=400)
canvas.pack()

line=canvas.create_line(randint(0,400),randint(0,400),randint(0,400),randint(0,400),fill="blue")
line_id=canvas.coords(line)
lx,ly=line_id[2],line_id[3]
for i in range(20):
    line=canvas.create_line(lx,ly,randint(0,400),randint(0,400),fill="blue")
    line_id=canvas.coords(line)
    lx,ly=line_id[2],line_id[3]
    
for i in range(20):
    line=canvas.create_line(lx,ly,randint(0,400),randint(0,400),fill="red")
    line_id=canvas.coords(line)
    lx,ly=line_id[2],line_id[3]






window.mainloop()