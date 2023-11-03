import tkinter
canvas = tkinter.Canvas()
canvas.pack()

for i in range(1,39):
 canvas.create_line(i*10,0,i*10,300)
 canvas.create_line(0,i*10,380,i*10)
