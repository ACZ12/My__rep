import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(-23422,-4234,2342,4234,fill='white')
canvas.create_oval(5,130,80,180,fill='brown')
canvas.create_rectangle(0,150,312332,324243224,fill='blue')
canvas.create_line(100,120,130,160)
canvas.create_line(130,160,210,160)
canvas.create_line(100,120,250,120)
canvas.create_line(210,160,250,120)
canvas.create_line(150,120,150,50)
canvas.create_line(150,120,150,50)
canvas.create_line(150,100,180,70)
canvas.create_line(180,70,150,50)
canvas.create_line(40,130,40,30)
canvas.create_rectangle(40,30,100,80,fill='green')
canvas.create_oval(50,40,90,70,fill='yellow',outline='green')
canvas.create_oval(60,40,100,70,fill='green',outline='green')

def hold(q,w):
 canvas.create_oval(q-25,w-25,q+25,w+25,fill='yellow',outline='yellow')
 canvas.create_oval(q-15,w-25,q+35,w+25,fill='white',outline='white')

def hold_tukorkep(q,w):
 canvas.create_oval(q-25,w-25,q+25,w+25,fill='yellow',outline='yellow')
 canvas.create_oval(q-15,w-25,q+35,w+25,fill='blue',outline='blue')

r=random.randint(0,150)
hold(300,150-r)
hold_tukorkep(300,150+r)
