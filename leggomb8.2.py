import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

szinek='red','green','orange','yellow','blue','purple','pink'

canvas.create_oval(20,120,50,150,fill=random.choice(szinek))
canvas.create_oval(40,120,70,150,fill=random.choice(szinek))
canvas.create_oval(60,120,90,150,fill=random.choice(szinek))
canvas.create_oval(80,120,110,150,fill=random.choice(szinek))
canvas.create_oval(100,120,130,150,fill=random.choice(szinek))
canvas.create_oval(120,120,150,150,fill=random.choice(szinek))
canvas.create_oval(140,120,170,150,fill=random.choice(szinek))
canvas.create_oval(160,120,190,150,fill=random.choice(szinek))

canvas.create_line(35,120,100,20)
canvas.create_line(55,120,100,20)
canvas.create_line(75,120,100,20)
canvas.create_line(95,120,100,20)
canvas.create_line(115,120,100,20)
canvas.create_line(135,120,100,20)
canvas.create_line(155,120,100,20)
canvas.create_line(175,120,100,20)
