import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def labda():
    canvas.delete('all')
    global y
    canvas.create_oval(x-5, y-5, x+5, y+5)
    y = y+5
    if y>250:
        y = 5
    if tovabb == 1:
        canvas.after(100, labda)

def stop(koorinatak):
    global tovabb
    tovabb = 0
    
tovabb = 1  
x = 200
y = 5
labda()
canvas.bind('<Button-1>',stop)
