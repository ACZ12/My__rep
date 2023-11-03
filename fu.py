from tkinter import *
import tkinter as tk
window=Tk()
canvas = Canvas()
canvas.pack()

def vonal(koordinatak):
 x = koordinatak.x
 y = koordinatak.y
 canvas.create_line(x,y,200,270,fill='green',width=3)

canvas.bind('<Button-1>',vonal)

window.mainloop()