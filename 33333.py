
import tkinter
import random
canvas = tkinter.Canvas(height=350)
canvas.pack()

a=1
b=35
e=[i for i in range(a,b+1)]
random.shuffle(e)
canvas.create_text(20,20,text=e)
