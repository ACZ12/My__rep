import tkinter
from random import *
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

def mozdony(q,w):
    canvas.create_rectangle(q,w,q+60,w+50,fill='green')
    canvas.create_rectangle(q+30,w-20,q+60,w,fill='red')
    canvas.create_rectangle(q+10,w-10,q+20,w,fill='blue')
    canvas.create_oval(q,w+40,q+25,w+65,fill='black')
    canvas.create_oval(q+25,w+40,q+50,w+65,fill='black')
    canvas.create_oval(q+50,w+40,q+75,w+65,fill='black')

def vonat(x,y):
    canvas.create_rectangle(x,y,x+80,y+50,fill='lightgreen')
    canvas.create_rectangle(x+5,y+5,x+35,y+30,fill='darkblue')
    canvas.create_rectangle(x+45,y+5,x+75,y+30,fill='darkblue')
    canvas.create_line(x,y+20,x-10,y+20)
    canvas.create_oval(x+5,y+40,x+30,y+65,fill='black')
    canvas.create_oval(x+35,y+40,x+60,y+65,fill='black')

mozdony(50,50)

q=30
w=50

for i in range(1,5):
 q=q+90
 vonat(q,w)
 
