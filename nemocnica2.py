import tkinter
canvas=tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(10,10,210,210,fill='darkblue')
canvas.create_rectangle(20,20,50,160,fill='white')
canvas.create_rectangle(170,20,200,160,fill='white')
canvas.create_rectangle(30,80,190,100,fill='white',outline='white')
canvas.create_text(110,180,text='NEMOCNICA',fill='white',font='Arial 25 bold')
