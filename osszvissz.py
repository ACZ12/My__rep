import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

for i in range(1,51):
    
 q=random.randint(1,5)
 e='red','green','orange','yellow','blue','purple','pink'

 canvas.create_line(1,random.randint(1,300),400,random.randint(1,300),width=q,fill=random.choice(e))
