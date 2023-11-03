import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_rectangle(10,10,120,150,fill='darkblue')

canvas.create_rectangle(20,20,110,110,fill='white')

canvas.create_text(65,60,text='Polícia' ,font='Arial 20 bold')
