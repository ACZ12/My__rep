import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def babu(q,w):
    canvas.create_oval(q,w,q+40,w+40,fill='red')
    canvas.create_line(q+20,w+40,q-30,w+150,width=2)
    canvas.create_line(q-30,w+150,q+70,w+150,width=2)
    canvas.create_line(q+20,w+40,q+70,w+150,width=2)
    canvas.create_rectangle(q,w+150,q+15,w+200,fill='red')
    canvas.create_rectangle(q+25,w+150,q+40,w+200,fill='red')

babu(100,20)
