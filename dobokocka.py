import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()

def negyzet(x, y, szam):

    canvas.create_rectangle(x-10, y-10, x+10, y+10)

    canvas.create_text(x, y, text=szam)


def button1_klikk():

    negyzet(randrange(300), randrange(200), randrange(100))


def button2_klikk():

    for i in range (1, 11):

        negyzet(i*20, 100, i)

        

button1 = tkinter.Button(text='Négyzet', command=button1_klikk)

button1.pack()

button2 = tkinter.Button(text='10 négyzet', command=button2_klikk)

button2.pack()




