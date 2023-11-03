import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def negyzet():
    x=0
    y=200
    
    for i in range(0,8):
     x=x+10
     y=y-10
     canvas.create_rectangle(x,y,x+i*10,y+i*10)
     x=x+i*10-10
     
negyzet()
