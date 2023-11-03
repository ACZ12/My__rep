import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

szinek='red','green','orange','yellow','blue','purple','pink'

canvas.create_oval(20,20,50,50,fill=random.choice(szinek))
canvas.create_oval(40,20,70,50,fill=random.choice(szinek))
canvas.create_oval(60,20,90,50,fill=random.choice(szinek))
canvas.create_oval(80,20,110,50,fill=random.choice(szinek))
canvas.create_oval(100,20,130,50,fill=random.choice(szinek))
canvas.create_oval(120,20,150,50,fill=random.choice(szinek))
canvas.create_oval(140,20,170,50,fill=random.choice(szinek))
canvas.create_oval(160,20,190,50,fill=random.choice(szinek))

canvas.create_line(35,50,100,200)
canvas.create_line(55,50,100,200)
canvas.create_line(75,50,100,200)
canvas.create_line(95,50,100,200)
canvas.create_line(115,50,100,200)
canvas.create_line(135,50,100,200)
canvas.create_line(155,50,100,200)
canvas.create_line(175,50,100,200)
