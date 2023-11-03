import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def var(q,w):
    canvas.create_rectangle(q,w,q+290,w+70)
    canvas.create_rectangle(q+70,w-30,q+100,w,fill='red')
    canvas.create_rectangle(q+130,w-30,q+160,w,fill='red')
    canvas.create_rectangle(q+190,w-30,q+220,w,fill='red')
    canvas.create_line(q,w,q+30,w-60)
    canvas.create_line(q+30,w-60,q+60,w)
    canvas.create_line(q+230,w,q+260,w-60)
    canvas.create_line(q+260,w-60,q+290,w)
    canvas.create_oval(q+30,w+20,q+60,w+50,fill='blue')
    canvas.create_oval(q+220,w+20,q+250,w+50,fill='blue')


var(20,80)
