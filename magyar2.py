import tkinter
canvas=tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(10,10,180,50,fill='red')
canvas.create_rectangle(10,50,180,90,fill='white')
canvas.create_rectangle(10,90,180,130,fill='green')

