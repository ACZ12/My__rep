import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_rectangle(10,10,190,50,fill='red')

canvas.create_rectangle(10,50,190,90,fill='white')

canvas.create_rectangle(10,90,190,130,fill='green')

canvas.mainloop()