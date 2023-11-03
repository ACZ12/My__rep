import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_rectangle(10,10,190,30,fill='blue')

canvas.create_rectangle(10,30,190,100,fill='white')

canvas.create_rectangle(10,100,190,120,fill='blue')

canvas.create_line(60,50,140,50,fill='blue',width=5)

canvas.create_line(60,80,140,80,fill='blue',width=5)

canvas.create_line(60,50,100,95,fill='blue',width=5)

canvas.create_line(100,95,140,50,fill='blue',width=5)

canvas.create_line(60,80,100,35,fill='blue',width=5)

canvas.create_line(100,35,140,80,fill='blue',width=5)
