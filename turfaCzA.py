from turtle import*
window=Screen()
t=Turtle()

t.width(30)

def fa1():
    t.penup()
    t.goto(-200,0)
    
    
    for i in range(2):
        t.seth(0)
        t.pendown()
        t.color("green")
        t.begin_fill()
        for i in range(3):
            t.fd(60)
            t.lt(120)
        t.end_fill()
        t.fd(30)
        t.seth(270)
        t.color("brown")
        t.fd(100)
        t.penup()
        t.bk(100)
        t.goto(150,0)

def fa2():
    t.penup()
    t.goto(0,-100)
    t.seth(90)
    for i in range(2):
        t.pendown()
        t.fd(100)
        t.dot(100,"green")
        t.penup()
        t.goto(300,-100)
        

fa1()
fa2()

#window.mainloop()
