from tkinter import *

window = Tk()
canvas = Canvas(window, height=400, width=900)
canvas.pack()

x = 100
y = 100

def tank1(x, y):
    canvas.create_rectangle(x - 20, y - 10, x + 20, y, tags="t1")

def left(event):
    global x, y
    if x > 10:
        x -= 10
        #y = 0
        canvas.move("t1", -10, 0)

def right(event):
    global x, y
    if x < 890:
        x += 10
        #y = 0
        canvas.move("t1", 10, 0)
        
a=5
b=-2
def apply_gravity(projectile):
    global a,b
    canvas.move(projectile, a, b)
    window.after(20, apply_gravity, projectile)
    b+=0.05

def shoot(event):
    global x,y,a,b
    a=5
    b=-2
    projectile = canvas.create_oval(x - 2, y - 2, x + 2, y + 2)
    apply_gravity(projectile)
    
window.bind("<a>", left)
window.bind("<d>", right)
window.bind("<space>", shoot)
tank1(x, y)










window.mainloop()
