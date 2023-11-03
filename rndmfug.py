import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()

for i in range(1,6):

 canvas.create_line(i*10, 10, i*10, 200)

