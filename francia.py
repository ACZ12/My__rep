import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_rectangle(10,10,70,130,fill='red')

canvas.create_rectangle(70,10,130,130)

canvas.create_rectangle(130,10,190,130,fill='blue')
