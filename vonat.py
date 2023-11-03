import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def vonat(x,y):
    canvas.create_rectangle(x,y,x+80,y+50,fill='lightgreen')
    canvas.create_rectangle(x+5,y+5,x+35,y+30,fill='darkblue')
    canvas.create_rectangle(x+45,y+5,x+75,y+30,fill='darkblue')
    canvas.create_line(x,y+20,x-10,y+20)
    canvas.create_oval(x,y+40,x+30,y+70,fill='black')
    canvas.create_oval(x+50,y+40,x+80,y+70,fill='black')

q=10
w=20

for i in range(1,5):
 q=q+90
 vonat(q-80,w)
 
