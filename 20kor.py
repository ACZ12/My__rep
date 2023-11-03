import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

r=0
szinek='red','green','blue','yellow','orange','pink','brown','purple'

def oval(q,w):
 e=random.randint(50,100)
 canvas.create_oval(q-e,w-e,q+e,w+e,outline=random.choice(szinek),width=3)

for i in range(1,21):
 r=r+30
 oval(50+r,130)



 
