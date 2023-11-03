import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()

for i in range(1,5):

 canvas.create_line(i*10, i*10, 200, i*10)

canvas.update()

canvas.after(1000)
