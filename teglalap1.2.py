import tkinter
canvas=tkinter.Canvas()
canvas.pack()

canvas.create_line(20,20,200,20,fill='green',width=10)
canvas.create_line(20,20,20,100,fill='gray',width=10)
canvas.create_line(200,20,200,100,fill='green',width=10)
canvas.create_line(20,100,200,100,fill='gray',width=10)
