import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()

for i in range(1,5):

 canvas.create_line(10, i*20, 400, i*30)

canvas.update()

canvas.after(1000)
