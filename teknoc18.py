import turtle
ablak=turtle.Screen()
t=turtle.Turtle()
t.speed(50)

a=1

for i in range(5):

    for i in range(200):
        t.fd(10)
        t.rt(a)
        a=a+0.2
    t.lt(176)
    for i in range(200):
        t.fd(10)
        t.lt(a)
        a=a-0.2
