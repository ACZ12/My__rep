import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_oval(30,70,70,110,fill='red')
canvas.create_oval(40,80,80,120,fill='green')
canvas.create_oval(20,80,60,120,fill='yellow')
canvas.create_rectangle(20,100,80,120,fill='white')
canvas.create_line(20,120,48,190)
canvas.create_line(80,120,48,190)
