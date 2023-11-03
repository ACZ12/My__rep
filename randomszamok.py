import tkinter

import random

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_text(50,50,text=random.randint(1,50))

canvas.create_text(60,60,text=random.randint(1,50))

canvas.create_text(70,70,text=random.randint(1,50))

canvas.create_text(80,80,text=random.randint(1,50))

canvas.create_text(90,90,text=random.randint(1,50))

canvas.create_text(100,100,text=random.randint(1,50))
