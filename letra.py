import tkinter
canvas = tkinter.Canvas()
canvas.pack()

w=0
q=0

for i in range(1,11):
 w=w+10
 canvas.create_line(50+w,i*20,100+w,i*20)

for i in range(1,3):
  q=q+30
  canvas.create_line(35+q,15,130+q,205)
