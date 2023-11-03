import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_oval(150,60,220,130,fill='beige')

canvas.create_oval(150,10,220,60,fill='black')

canvas.create_oval(135,50,235,75,fill='black')

canvas.create_rectangle(150,130,220,200,fill='green')

canvas.create_rectangle(185,102,205,105,fill='black')

canvas.create_rectangle(160,80,170,90,fill='black')

canvas.create_rectangle(200,80,210,90,fill='black')

canvas.mainloop()