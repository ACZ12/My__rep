import tkinter
canvas=tkinter.Canvas(bg='white')
import random
canvas.pack()

x=random.randrange(200)
y=random.randrange(200)
x2=x+50
canvas.create_line(x,y,x2,y)

print(x,y,x2,y)
