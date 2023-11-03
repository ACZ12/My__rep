import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()

x=100

y=0

for i in range(1,9):

 y=y+25

 canvas.create_rectangle(x,y,x+200,y+15)
