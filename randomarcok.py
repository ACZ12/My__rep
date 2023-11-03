import tkinter
from random import *
canvas = tkinter.Canvas(height=300,width=600)
canvas.pack()

def arc(x,y):
    canvas.create_rectangle(y,x,y+90,x+90)
    canvas.create_rectangle(y+10,x+10,y+30,x+30)
    canvas.create_rectangle(y+60,x+10,y+80,x+30)
    canvas.create_rectangle(y+30,x+30,y+60,x+65)



arc(10,10)
