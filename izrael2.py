import tkinter
canvas=tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(10,10,180,130,fill='blue')
canvas.create_rectangle(10,35,180,105,fill='white')

canvas.create_line(95,40,125,85,fill='blue',width=3)
canvas.create_line(95,40,65,85,fill='blue',width=3)
canvas.create_line(125,85,65,85,fill='blue',width=3)

canvas.create_line(65,55,95,100,fill='blue',width=3)
canvas.create_line(95,100,125,55,fill='blue',width=3)
canvas.create_line(125,55,65,55,fill='blue',width=3)
