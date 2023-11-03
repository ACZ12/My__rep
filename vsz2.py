import tkinter
canvas=tkinter.Canvas(bg='white')
import random
canvas.pack()

a=20
for i in range(6):
 canvas.create_text(40+a,60,text=random.randint(0,50))
 a=a+20
