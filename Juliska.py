import tkinter
canvas=tkinter.Canvas()
canvas.pack()

def Juliska(x,y):
    canvas.create_oval(x,y,x+50,y+50,fill='red')
    canvas.create_line(x+25,y+50,x-20,y+170)
    canvas.create_line(x+25,y+50,x+70,y+170)
    canvas.create_line(x-20,y+170,x+70,y+170)
    canvas.create_rectangle(x,y+170,x+20,y+230,fill='red')
    canvas.create_rectangle(x+30,y+170,x+50,y+230,fill='red')

    

Juliska(50,30)

