import tkinter
canvas = tkinter.Canvas()
canvas.pack()

for i in range(1,85):
 canvas.create_line(1,1,i*5,300,fill='green')
 canvas.create_line(385,270,i*5,1,fill='blue')
