import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()

y=10

for i in range(1,6):

 y=y+40

 canvas.create_line(y,y,y+40,y)

 canvas.create_line(y,y-40,y,y)
