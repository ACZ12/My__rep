import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()

x=0

for i in range(1,9):

 x=x+45

 canvas.create_text(170,130,text='Python' ,font='Arial 40 bold',angle=x)
