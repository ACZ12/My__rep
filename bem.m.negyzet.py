import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def negyzet(x,y,szam):
    canvas.create_rectangle(x-10,y-10,x+10,y+10)

def button1cl():
    negyzet(randrange(200),randrange(200),randrange(200))
    

button1=tkinter.Button(text='Négyzet',command=button1cl)
button1.pack()
