import turtle
import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(master = root, width = 500, height = 300)
canvas.pack()

t = turtle.RawTurtle(canvas)


canvas.create_rectangle(-250,-150,250,-50,fill="blue",width=0)
canvas.create_rectangle(-250,50,250,150,fill="black",width=0)
canvas.create_rectangle(0,0,250,150,fill="cyan",width=0)
canvas.create_line(-250,150,250,-150,fill="white",width=15)

t.ht()
t.setpos(-50,12.5)
t.color("black")
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.rt(144)
t.end_fill()


root.mainloop()