from tkinter import *
root=Tk()
root.geometry("500x500")
canvas=Canvas(width=400, height=400)
canvas.pack()

canvas.create_rectangle(0,0,400,400,fill='yellow')

root.mainloop()


