import tkinter as tk
canvas=tk.Canvas(height=600,width=600)
canvas.pack()
canvas.create_line(200,0,200,600)
canvas.create_line(400,0,400,600)
canvas.create_line(0,200,600,200)
canvas.create_line(0,400,600,400)


def cross(xy):
    x=xy.x
    y=xy.y
    canvas.create_line(x-50,y-50,x+50,y+50)
    canvas.create_line(x-50,y+50,x+50,y-50)

def oval(xy):
    x=xy.x
    y=xy.y
    canvas.create_oval(x-50,y-50,x+50,y+50)


a=1

if a==1:
    canvas.bind("<Button-1>",cross)
    a-=1
else:
    canvas.bind("<Button-1>",oval)
    a+=1
    
canvas.mainloop()