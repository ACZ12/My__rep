import tkinter
canvas=tkinter.Canvas()
canvas.pack()


canvas.create_oval(10,10,210,210,fill='red')
canvas.create_oval(30,30,190,190,fill='white')
canvas.create_text(110,110,text='6 t',font='Arial 70 bold')
