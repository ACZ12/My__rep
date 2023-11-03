import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_oval(10,10,200,200,fill='red')

canvas.create_oval(30,30,180,180,fill='white')

canvas.create_text(100,100,text='6 t',font='Arial 70 bold')
