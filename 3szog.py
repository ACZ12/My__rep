import tkinter
canvas=tkinter.Canvas()
canvas.pack()

canvas.create_line(20,100,130,100,fill='blue')
canvas.create_line(20,100,70,30,fill='blue')
canvas.create_line(70,30,120,100,fill='blue')

canvas.create_line(70,100,170,100,fill='red')
canvas.create_line(70,100,120,30,fill='red')
canvas.create_line(120,30,170,100,fill='red')
