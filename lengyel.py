import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_rectangle(10,10,190,65,fill='red')

canvas.create_rectangle(10,65,190,120)

canvas.mainloop()
