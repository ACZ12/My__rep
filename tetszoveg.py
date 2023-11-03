import tkinter
from tkinter import *
canvas = Canvas()
canvas.pack()

def szoveg(eger):
    sz=entry1.get()
    me=int(entry2.get())
    for i in range(me):
     canvas.create_text(eger.x,eger.y,text=sz,font='Ariel 20 bold',angle=(360/me)*i)
    


canvas.bind_all('<Button-1>',szoveg)
entry1=tkinter.Entry()
entry1.pack()
entry2=tkinter.Entry()
entry2.pack()
