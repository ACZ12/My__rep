import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_rectangle(10,10,200,200,fill='red')

canvas.create_rectangle(80,40,125,170,fill='white',outline='white')

canvas.create_rectangle(40,80,170,125,fill='white',outline='white')
