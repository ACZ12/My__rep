from tkinter import *
root=Tk()
canvas=Canvas(root)
canvas.pack()

def irdki(event):
    print (event.keysym)

canvas.bind_all("<Key>",irdki)
root.mainloop()

import keyboard
while 1:
    if keyboard.is_pressed("1"):
        print("1")