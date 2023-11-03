import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kor(koordinatak):
 x = koordinatak.x
 y = koordinatak.y
 canvas.create_line(x-30, y, x+30, y)
 canvas.create_line(x, y-30, x, y+60)

canvas.bind('<Button-1>',kor)
