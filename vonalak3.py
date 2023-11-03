import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def rajz(koorinatak):
    x=koorinatak.x
    y=koorinatak.y
    szin=choice(('deepskyblue','skyblue','blue','navy','royalblue','dodgerblue','aqua','cyan','cornflowerblue','lightblue'))
    mennyiseg=int(entry1.get())
    hely=int(entry2.get())
    hossz=entry3.get()
    q=0
    for i in range(0,mennyiseg):
     q=q+hely
     canvas.create_line(x+q,y-15,x+q,y+hossz,fill=szin)

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

canvas.bind('<Button-1>',rajz)


