import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(10,60,100,200,fill='lightgreen')
canvas.create_rectangle(100,110,180,200,fill='orange')
canvas.create_rectangle(20,70,50,100,fill='blue')
canvas.create_rectangle(60,70,90,100,fill='blue')
canvas.create_rectangle(20,110,50,140,fill='blue')
canvas.create_rectangle(60,110,90,140,fill='blue')
canvas.create_rectangle(110,120,130,140,fill='blue')
canvas.create_rectangle(140,120,160,140,fill='blue')
canvas.create_rectangle(60,150,90,200,fill='black')
canvas.create_rectangle(140,160,170,200,fill='black')
canvas.create_rectangle(230,150,250,200,fill='brown')
canvas.create_rectangle(305,150,325,200,fill='brown')
canvas.create_line(10,60,55,20,fill='red',width='3')
canvas.create_line(55,20,100,60,fill='red',width='3')
canvas.create_oval(205,90,275,160,fill='green')
canvas.create_oval(280,90,350,160,fill='green')
