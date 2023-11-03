import tkinter
import random
canvas = tkinter.Canvas(height=350)
canvas.pack()

deck=list(range(1,7))
y=20

for i in range(1):
 y=y+30
 hand=random.sample(deck,k=1)
 canvas.create_text(100,y,text=hand)





