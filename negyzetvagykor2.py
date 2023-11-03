import tkinter
canvas=tkinter.Canvas(height=600,width=400)
canvas.pack()

canvas.create_line(0,300,400,300)

def alakzat(eger):
    if eger.y<300:
     canvas.create_rectangle(eger.x-10,eger.y-10,eger.x+10,eger.y+10)
    else:
     canvas.create_oval(eger.x-10,eger.y-10,eger.x+10,eger.y+10)


canvas.bind_all('<Button-1>',alakzat)
