import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_rectangle(10,10,200,260,fill='darkblue')

canvas.create_text(105,90,text='P',font='Arial 80 bold',fill='white')

canvas.create_text(105,190,text='RÉSERVÉ',font='Arial 30 bold',fill='white')
