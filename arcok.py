import tkinter
canvas=tkinter.Canvas()
import random
canvas.pack()

e='red','green','blue','yellow','brown'
q=random.randrange(10,30)

def arc(x,y):
    canvas.create_rectangle(x,y,x+100,y+100)
    
    canvas.create_rectangle(x+40,y+40,x+40-q,y+40-q,fill=random.choice(e))
    canvas.create_rectangle(x+60,y+40,x+60+q,y+40-q,fill=random.choice(e))

    canvas.create_rectangle(x+50-q*0.5,y+40,x+50+q*0.5,y+70,fill=random.choice(e))

    canvas.create_rectangle(x+20,y+85-q*0.5,x+80,y+85+q*0.5,fill=random.choice(e))

for i in range(3):
    arc(i*120+20,20)
