import tkinter
canvas = tkinter.Canvas(height=400)
canvas.pack()

def labda():
    canvas.delete('all')
    global y
    canvas.create_oval(x-5,y-5,x+5,y+5)

    y=y+5
    if y<400:
     canvas.after(100,labda)
    else:
     canvas.delete('all')
     y=5
     canvas.create_oval(x-5,y-5,x+5,y+5)
     canvas.after(100,labda)
     
x=70
y=5
labda()
