import tkinter
from random import *
canvas=tkinter.Canvas()
canvas.pack()

def auto(y,x):
    canvas.create_rectangle(y,x,y+250,x+70,fill='red')
    canvas.create_rectangle(y,x,y+30,x+20,fill='yellow')
    canvas.create_rectangle(y+80,x,y+170,x-70,fill='blue')
    canvas.create_line(y+40,x,y+60,x-70,width=3,fill='red')
    canvas.create_line(y+210,x,y+190,x-70,width=3,fill='red')
    canvas.create_line(y+60,x-70,y+190,x-70,width=3,fill='red')
    canvas.create_line(y+210,x,y+190,x-70,width=3,fill='red')
    canvas.create_line(y+210,x,y+190,x-70,width=3,fill='red')
    canvas.create_oval(y+30,x+50,y+80,x+100,fill='black')
    canvas.create_oval(y+170,x+50,y+220,x+100,fill='black')

auto(20,100)
                            
