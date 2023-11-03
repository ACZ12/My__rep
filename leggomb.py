import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(70,100,130,110,fill='red')
canvas.create_line(100,100,70,30,width=2)
canvas.create_line(100,100,130,30,width=2)
canvas.create_oval(70,10,130,60,width=2,fill='blue')
