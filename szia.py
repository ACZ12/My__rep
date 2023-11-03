import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_text(100, 70, text='Szia', fill='blue')

canvas.create_text(200, 50, text='Python', font='Arial 70 bold', fill='red')
