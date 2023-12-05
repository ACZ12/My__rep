import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def ird_ki(koorinatak):
    x=koorinatak.x
    y=koorinatak.y
    mennyiseg=int(entry1.get())
    hely=int(entry2.get())
    hossz=int(entry3.get())
    szin = ['lightblue','cyan','blue','darkblue',"navyblue"]

    w=0
    for i in range(0,mennyiseg):
        w+=hely
        canvas.create_line(x+w,y-hossz/2,x+w,y+hossz/2,fill=choice(szin))

def torles():
    canvas.delete('all')

button1=tkinter.Button(text='Törlés', command=torles)
button1.pack()
entry1=tkinter.Entry()
entry1.pack()
entry2=tkinter.Entry()
entry2.pack()
entry3=tkinter.Entry()
entry3.pack()
canvas.bind('<Button-1>',ird_ki)
canvas.mainloop()