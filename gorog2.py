import tkinter
canvas=tkinter.Canvas()
canvas.pack()

a=10

for i in range(4):
     canvas.create_rectangle(10,10+a,180,20+a,fill='darkblue',outline='darkblue')
     
     canvas.create_rectangle(10,20+a,180,30+a,fill='white',outline='white')
     a=a+20
     
canvas.create_rectangle(10,100,180,110,fill='darkblue',outline='darkblue')

canvas.create_rectangle(10,20,60,70,fill='white',outline='white')
canvas.create_rectangle(10,20,30,40,fill='darkblue',outline='darkblue')
canvas.create_rectangle(10,50,30,70,fill='darkblue',outline='darkblue')
canvas.create_rectangle(40,20,60,39,fill='darkblue',outline='darkblue')
canvas.create_rectangle(40,50,60,69,fill='darkblue',outline='darkblue')
