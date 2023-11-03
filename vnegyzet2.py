import tkinter
canvas=tkinter.Canvas(bg='white')
import random
canvas.pack()


x=random.randrange(200)
y=random.randrange(200)
q=random.randrange(200)
canvas.create_rectangle(x,y,x+q,y+q,fill='red')

canvas.create_text(x+0.5*q,y+0.5*q,text=q)

