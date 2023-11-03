import turtle
ablak=turtle.Screen()
t=turtle.Turtle()

t.penup()
t.goto(-300,0)
t.seth(180)
t.pendown()
t.circle(100)

t.penup()
t.goto(250,0)
t.pendown()
t.lt(90)
t.circle(100)


t.penup()
t.goto(0,0)
t.pendown()


for i in range(7):

    for i in range(20):
        t.fd(11)
        t.rt(5)
        
    t.rt(140)
