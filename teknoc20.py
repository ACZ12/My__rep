import turtle
import random
ablak=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
t6=turtle.Turtle()
t7=turtle.Turtle()
t8=turtle.Turtle()

t2.rt(45)
t3.rt(90)
t4.rt(135)
t5.rt(180)
t6.rt(225)
t7.rt(270)
t8.rt(315)

t1.color('red')
t2.color('blue')
t3.color('green')
t4.color('purple')
t5.color('pink')
t6.color('yellow')
t7.color('brown')
t8.color('cyan')

t1.pensize(5)
t2.pensize(5)
t3.pensize(5)
t4.pensize(5)
t5.pensize(5)
t6.pensize(5)
t7.pensize(5)
t8.pensize(5)

a=40

for i in range(20):
        b=random.randint(0,40)
        t1.fd(a)
        t1.rt(b)

        b=random.randint(0,40)
        t2.fd(a)
        t2.rt(b)

        b=random.randint(0,40)
        t3.fd(a)
        t3.rt(b)

        b=random.randint(0,40)
        t4.fd(a)
        t4.rt(b)

        b=random.randint(0,40)
        t5.fd(a)
        t5.rt(b)

        b=random.randint(0,40)
        t6.fd(a)
        t6.rt(b)

        b=random.randint(0,40)
        t7.fd(a)
        t7.rt(b)

        b=random.randint(0,40)
        t8.fd(a)
        t8.rt(b)
        a=a-1
