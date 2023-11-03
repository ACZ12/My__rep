import tkinter
canvas=tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(10,10,150,150,fill='red')
canvas.create_rectangle(40,65,120,95,fill='white',outline='white')
canvas.create_rectangle(65,40,95,120,fill='white',outline='white')

