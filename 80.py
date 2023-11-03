import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_oval(10,10,200,200,fill='red')

canvas.create_oval(30,30,180,180,fill='white')

canvas.create_text(105,105,text='80',font='Arial 70 bold')
