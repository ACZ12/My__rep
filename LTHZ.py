import tkinter
canvas=tkinter.Canvas()
canvas.pack()

canvas.create_line(20,20,20,100,fill='blue')
canvas.create_line(20,100,70,100,fill='orange')

canvas.create_line(100,20,150,20,fill='blue')
canvas.create_line(125,20,125,100,fill='green')

canvas.create_line(180,20,180,100,fill='red')
canvas.create_line(230,20,230,100,fill='black')
canvas.create_line(180,60,230,60,fill='blue')

canvas.create_line(260,20,310,20,fill='orange')
canvas.create_line(310,20,260,100,fill='blue')
canvas.create_line(260,100,310,100,fill='green')
