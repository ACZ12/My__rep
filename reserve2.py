import tkinter
canvas=tkinter.Canvas()
canvas.pack()


canvas.create_rectangle(10,10,160,210,fill='darkblue')
canvas.create_text(85,90,text='P',font='Ariel 80 bold',fill='white')
canvas.create_text(85,180,text='RÉSERVÉ',font='Ariel 20 bold',fill='white')

