from tkinter import *

canvas = Canvas(height=400,width=400,bg='white')
canvas.pack()

def vonal(eger):

 if eger.x < 200 and eger.y < 200:
     canvas.create_line(200,200,eger.x,eger.y,fill='red',width=3)

 elif eger.x > 200 and eger.y < 200:
    canvas.create_line(200,200,eger.x,eger.y,fill='green',width=3)

 elif eger.x <  200 and eger.y > 200:
    canvas.create_line(200,200,eger.x,eger.y,fill='blue',width=3)

 else:

    canvas.create_line(200,200,eger.x,eger.y,fill='yellow',width=3)

canvas.bind_all('<Button-1>',vonal)
