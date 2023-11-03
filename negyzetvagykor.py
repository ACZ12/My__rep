from tkinter import *

canvas = Canvas(height=400,width=640,bg='white')
canvas.create_line(0,200,640,200,width=5)
canvas.pack()

def alakzat(eger):
    if eger.y < 200:
        canvas.create_rectangle(eger.x-15,eger.y-15,eger.x+15,eger.y+15,fill='blue')
    else:
        canvas.create_oval(eger.x-15,eger.y-15,eger.x+15,eger.y+15,fill='yellow')
    

canvas.bind_all('<Button-1>',alakzat)


