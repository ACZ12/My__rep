import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_line(110, 10, 10, 200, fill='blue')

canvas.create_line(10, 200, 210, 200, fill='blue')

canvas.create_line(210, 200, 110, 10, fill='blue')

canvas.create_line(140, 10, 40, 200, fill='red')

canvas.create_line(40, 200, 240, 200, fill='red')

canvas.create_line(240, 200, 140, 10, fill='red')

canvas.mainloop()