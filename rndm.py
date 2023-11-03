import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()

for i in range(1,6):

 canvas.create_line(10, i*10, 200, i*20)

