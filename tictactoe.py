import tkinter
canvas = tkinter.Canvas(width=800)
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

canvas.create_text(600,60,text='Tic Tac Toe\nAz a játekos nyer,aki vizszintesen,\nfüggőlegesen vagy átlósan 5 egyformát \ntesz egymás mellé.\nA kört a bal egérgombbal,\na négyzetet a jobb egérgombbal\nlehet kattintani.',fill='green',font='Arial 15 bold')


canvas.mainloop()