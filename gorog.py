import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_rectangle(10,10,60,60,fill='darkblue',outline='darkblue')

canvas.create_rectangle(30,10,40,60,fill='white',outline='white')

canvas.create_rectangle(10,30,60,40,fill='white',outline='white')

canvas.create_rectangle(60,10,160,20,fill='darkblue',outline='darkblue')

canvas.create_rectangle(60,20,160,30,fill='white',outline='white')

canvas.create_rectangle(60,30,160,40,fill='darkblue',outline='darkblue')

canvas.create_rectangle(60,40,160,50,fill='white',outline='white')

canvas.create_rectangle(60,50,160,60,fill='darkblue',outline='darkblue')

canvas.create_rectangle(10,60,160,70,fill='white',outline='white')

canvas.create_rectangle(10,70,160,80,fill='darkblue',outline='darkblue')

canvas.create_rectangle(10,80,160,90,fill='white',outline='white')

canvas.create_rectangle(10,90,160,100,fill='darkblue',outline='darkblue')
