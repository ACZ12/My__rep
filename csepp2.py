import tkinter
from random import * 
canvas = tkinter.Canvas(bg='white', width=400, height=600)
canvas.pack()

melyseg=500
y_csepp = 100
a=0
x=0

canvas.create_oval(60,20,80,40,fill='blue',tags='csepp')
canvas.create_oval(20,400,120,420)
canvas.create_oval(20,420,120,440)
canvas.create_line(20,410,20,430)
canvas.create_line(120,410,120,430)

def xkap():
    if x==0:
       x=1
    elif x==1:
          x=0

def mozgasd():
 if x==1:
    global x
    global a
    global y_csepp
    y_csepp = y_csepp+5
    canvas.move('csepp',0,5)
 elif y_csepp>melyseg:
        a=a+10
        canvas.create_oval(60-a,420,80+a,430,fill='blue',tags='tocsa')
        y_csepp = y_csepp - melyseg
        canvas.move('csepp',0,-melyseg)
 elif a>40:
        a=0
        canvas.delete('tocsa')
 print(y_csepp)   
 canvas.after(50,mozgasd)

button1=tkinter.Button(text='Start/Stop',command=xkap)
button1.pack()

