import tkinter
canvas = tkinter.Canvas(width=600,height=600)
canvas.pack()
from random import*


def rajzold_le(koordinatak):
    mennyiseg=(entry1.get())
   
    for i in range(int(mennyiseg)):
      x=randint(10,590)
      y=randint(10,590)
      canvas.create_oval(x-10,y-10,x+10,y+10)

entry1=tkinter.Entry()
entry1.pack()




canvas.bind('<Button-1>',rajzold_le)
