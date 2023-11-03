import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

for i in range(1,20):
 q=random.randint(1,3)
 canvas.create_rectangle(i*5, 10, i*5+q,100,fill='black')

 print (q)
