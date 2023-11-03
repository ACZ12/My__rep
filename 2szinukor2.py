import tkinter
from random import *
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()



def kor():
    x=250
    y=110
    a=110
    for i in range(0,10):
         a=a-10
         canvas.create_oval(x+a,y+a,x-a,y-a,fill='green')
         canvas.create_oval(x+a-5,y+a-5,x-a+5,y-a+5,fill='yellow')


kor()
