import tkinter
canvas=tkinter.Canvas()
canvas.pack()

def var(x,y):
    canvas.create_rectangle(x,y,x+300,y+80)
    canvas.create_rectangle(x+135,y,x+165,y-30,fill='red')
    canvas.create_rectangle(x+75,y,x+105,y-30,fill='red')
    canvas.create_rectangle(x+195,y,x+225,y-30,fill='red')
    canvas.create_line(x,y,x+25,y-50)
    canvas.create_line(x+250,y,x+275,y-50)
    canvas.create_line(x+25,y-50,x+50,y)
    canvas.create_line(x+275,y-50,x+300,y)
    canvas.create_oval(x+25,y+25,x+55,y+55,fill='blue')
    canvas.create_oval(x+245,y+25,x+275,y+55,fill='blue')
    

    
 
var(40,100)

