import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()

for i in range(1,11):

 canvas.create_line(i*10, 10, i*10, 200)

canvas.update()

canvas.after(1000)
