import tkinter
canvas=tkinter.Canvas(bg='white')
import random
canvas.pack()

c=('cyan','lightblue','darkred','yellow','darkgreen','brown','pink','salmon')
a=30
for i in range(11):
    canvas.create_rectangle(10+a,50,40+a,80,fill=random.choice(c))
    a=a+30

canvas.create_text(55,65,text='P',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(85,65,text='r',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(115,65,text='o',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(145,65,text='g',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(175,65,text='r',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(205,65,text='a',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(235,65,text='m',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(265,65,text='o',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(295,65,text='z',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(325,65,text='á',fill=random.choice(c),font='Arila 15 bold')
canvas.create_text(355,65,text='s',fill=random.choice(c),font='Arila 15 bold')
