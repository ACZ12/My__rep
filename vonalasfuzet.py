import tkinter
canvas = tkinter.Canvas(width=500,height=400)
canvas.pack()

canvas.create_rectangle(20,20,480,380)

for i in range(1,19):
 canvas.create_line(20,i*20,480,i*20)
 canvas.update()
 canvas.after(1000)
