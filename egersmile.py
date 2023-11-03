import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def smile(koordinatak):
 x = koordinatak.x
 y = koordinatak.y
 canvas.create_oval(x-30,y-30,x+30,y+30,fill='yellow')
 canvas.create_oval(x-20,y,x+20,y+20,fill='black')
 canvas.create_oval(x-20,y-10,x+20,y+15,fill='yellow',outline='yellow')
 canvas.create_oval(x-5,y-5,x-15,y-15,fill='white')
 canvas.create_oval(x+5,y-5,x+15,y-15,fill='white')

canvas.bind('<Button-1>',smile)
canvas.mainloop()