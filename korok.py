import tkinter
canvas = tkinter.Canvas(width=600,height=600)
canvas.pack()

w=10

def rajzold_le():
 global w
 q=10
 q=q+w
 mennyiseg=(entry1.get())
 for i in range(int(mennyiseg)):
    canvas.create_oval(20+q,20,40+q,40)
    w=w+10



entry1=tkinter.Entry()
entry1.pack()




canvas.bind('<Button-1>',rajzold_le)


