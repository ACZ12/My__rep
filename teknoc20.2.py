import turtle
import random
ablak=turtle.Screen()
t=turtle.getturtle()
t.speed(0)

f=0
o=100
s=('red','green','blue','yellow','brown','pink','purple','cyan','orange','grey','lightgreen')

for i in range(8):
    t=turtle.Turtle()
    t.turtlesize(2)
    t.ht()
    t.color(random.choice(s))
    t.width(5)
    t.up()
    t.seth(f)
    t.fd(20)
    t.rt(180)
    t.stamp()
    t.down()
    t.rt(180)
    f=f+45
    o=random.randint(10,30)

    
    for i in range(50):
        t.fd(random.randint(5,30))
        t.rt(o)
        o=o-1
        if o<0:
            o=0
