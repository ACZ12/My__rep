import tkinter
canvas=tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(10,10,160,210,fill='darkblue')
canvas.create_rectangle(20,20,150,160,fill='white')
canvas.create_text(85,90,text='Polícia',font='Arial 25 bold')
