import tkinter

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_oval(10,10,170,170,fill='red')

canvas.create_oval(30,30,150,150,fill='white')

canvas.create_text(90,90,text='80',font='Arial 70 bold')

canvas.create_rectangle(10,170,170,215,width=5)

canvas.create_text(90,195,text='22:00 - 04:00',font='Arial 19 bold')

canvas.create_rectangle(85,218,95,260,fill='grey',outline='grey')
