import tkinter
canvas=tkinter.Canvas()
import random
canvas.pack()

e='red','green','blue','yellow','brown'

def kocsi(x,y):
    canvas.create_rectangle(x,y,x+80,y+60,fill=random.choice(e))
    canvas.create_rectangle(x+5,y+5,x+35,y+35,fill='lightblue')
    canvas.create_rectangle(x+45,y+5,x+75,y+35,fill='lightblue')
    canvas.create_oval(x+5,y+50,x+35,y+80,fill='black')
    canvas.create_oval(x+45,y+50,x+75,y+80,fill='black')
    canvas.create_line(x-10,y+40,x,y+40,width=5)

for i in range(1,6):    
    kocsi(i*90-80,50)
    
