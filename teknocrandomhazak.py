import turtle
import random
ablak=turtle.Screen()
eszti=turtle.Turtle()
eszti.shape('arrow')



for i in range(20):
    a=(random.randrange(20,200))
    eszti.begin_fill()
    for i in range(4):
        eszti.fillcolor(random.choice(('red','green','blue','yellow','brown','pink','purple')))
        eszti.forward(a)
        eszti.right(90)
    eszti.end_fill()
    eszti.fillcolor(random.choice(('red','green','blue','yellow','brown','pink','purple')))
    eszti.begin_fill()    
    eszti.left(45)
    eszti.forward(a/1.42)
    eszti.right(90)
    eszti.forward(a/1.42)
    eszti.end_fill()
    eszti.penup()
    eszti.right(random.randrange(0,360))
    eszti.forward(random.randrange(100,200))
    eszti.pendown()

