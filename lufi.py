import tkinter
canvas=tkinter.Canvas()
import random
canvas.pack()

a=40
b='pink','orange','yellow','blue','green','red'

for i in range(8):
    canvas.create_oval(-20+a,30,40+a,90,fill=random.choice(b))
    canvas.create_line(10+a,90,190,260)
    a=a+40
    
