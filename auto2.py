import tkinter
canvas=tkinter.Canvas()
import random
canvas.pack()

a=5

for i in range(50):
    canvas.create_line(30+a,50,30+a,250,width=random.randrange(1,5))
    a=a+5
