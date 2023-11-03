import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kereszt(koordinatak):
    x=koordinatak.x
    y=koordinatak.y
    canvas.create_line(x-10,y,x+10,y)
    canvas.create_line(x,y-10,x,y+20)

canvas.bind('<Button-1>',kereszt)
