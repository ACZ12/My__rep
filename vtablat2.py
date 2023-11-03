import tkinter
canvas=tkinter.Canvas(bg='white')
import random
canvas.pack()


z=random.randrange(200)
w=random.randrange(200)
t=random.randrange(10,100,10)
canvas.create_oval(z-10,w-10,z+60,w+60,fill='red')
canvas.create_oval(z,w,z+50,w+50,fill='white')
canvas.create_text(z+25,w+25,text=t,font='Arial 20 bold')

