import tkinter
canvas=tkinter.Canvas(bg='white')
import random
canvas.pack()

x=random.randrange(200)
y=random.randrange(200)
tav=random.randint(30,100)
vas=random.randrange(20)
canvas.create_line(x,y,x+tav,y+tav,width=vas)


print(tav)
print(vas)
