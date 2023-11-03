import tkinter
canvas=tkinter.Canvas()
canvas.pack()


canvas.create_oval(10,10,110,110,fill='red')
canvas.create_oval(20,20,100,100,fill='white')
canvas.create_text(60,60,text=80,font='Ariel 50 bold')
canvas.create_rectangle(10,110,110,140)
canvas.create_text(60,125,text='22:00 - 04:00',font='Ariel 12 bold')
canvas.create_rectangle(55,141,65,180,outline='grey',fill='grey')
