import tkinter
import random
from random import*
canvas=tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(20,20,100,100)
canvas.create_text(70,70,text=('Hello world!'))

q=random.choice(1,2,3,4,5,6,7,8,9,10)

if q>5:
  print(q)
