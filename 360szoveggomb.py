import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()

def ird_ki(koorinatak):
    x=koorinatak.x
    y=koorinatak.y
    mennyiseg=int(entry1.get())
    szin = choice(('red','green','blue','yellow','black'))
    kimenet=entry2.get()
    for i in range(0,mennyiseg):
        canvas.create_text(x,y,text='             '+kimenet,
                       font='Arial 15',angle=i*360/mennyiseg,tag=kimenet,
                       fill=szin)

def torles():
    canvas.delete('all')

button1=tkinter.Button(text='Törlés', command=torles)
button1.pack()
entry1=tkinter.Entry()
entry1.pack()
entry2=tkinter.Entry()
entry2.pack()
canvas.bind('<Button-1>',ird_ki)
canvas.mainloop()