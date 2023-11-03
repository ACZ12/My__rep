import tkinter
canvas = tkinter.Canvas(width=500)
canvas.pack()

for i in range(1,7):
 canvas.create_line(i*40,40,i*40,240)
 canvas.create_line(40,i*40,240,i*40)



def negyzet(koordinatak):
 x = koordinatak.x
 y = koordinatak.y
 canvas.create_rectangle(x-10,y-10,x+10,y+10,fill='lightblue')

def kor(koordinatak):
 x = koordinatak.x
 y = koordinatak.y
 canvas.create_oval(x-10,y-10,x+10,y+10,fill='purple')


canvas.bind('<Button-3>',negyzet)
canvas.bind('<Button-1>',kor)

canvas.create_text(360,60,text='Tic Tac Toe',fill='green',font='Arial 15 bold')
canvas.create_text(360,90,text='Az a játekos nyer,aki vizszintesen,')
canvas.create_text(360,105,text='függőlegesen vagy átlósan 5 egyformát ')
canvas.create_text(360,120,text='tesz egymás mellé.')
canvas.create_text(360,135,text='A kört a bal egérgombbal,')
canvas.create_text(360,150,text='a négyzetet a jobb egérgombbal')
canvas.create_text(360,165,text='lehet kattintani.')

canvas.mainloop()