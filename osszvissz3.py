import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

for i in range(1,81):
    
 q=random.randint(1,5)
 e='red','green','orange','yellow','blue','purple','pink'

 canvas.create_line(150,150,random.randint(20,300),random.randint(20,300),width=q,fill=random.choice(e))
