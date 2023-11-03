import tkinter
canvas = tkinter.Canvas(bg='white', width=600, height=600)
canvas.pack()

canvas.create_oval(5,510,595,570,width=2)
canvas.create_oval(5,450,595,510,width=2)
canvas.create_line(595,480,595,540,width=2)
canvas.create_line(5,480,5,540,width=2)
canvas.create_oval(280,50,320,90,fill='blue',tags='csepp')

y_csepp=70
w=20
mukodj=1
c=0
e=True

def csepeges():
     if e==True:
          global w
          q=20
          q=q+w
          global c
          global mukodj
          global y_csepp
          if mukodj==1:
               y_csepp=y_csepp+5
               canvas.move('csepp',0,5)
               if y_csepp>510:
                    canvas.delete('szoveg')
                    q=q+w
                    c=c+1
                    y_csepp = y_csepp - 510
                    canvas.move('csepp',0,-510)
                    canvas.create_oval(250-q,520,350+q,540,fill='blue',tags='paca')
                    canvas.create_text(500,50,text='Cseppek száma: '+str(c),tags='szoveg',fill='green',)
                    w=w+40

               if q>270:
                    canvas.delete('paca')
                    q=0
                    w=w-160
                    c=0
               canvas.after(1,csepeges)

def stop():
     global e
     if e==True:
          e=False
     else:
          e=True
          csepeges()





button1=tkinter.Button(text='Start/Stop', command=stop)
button1.pack()
canvas.bind('<Button-1>',stop)
csepeges()

canvas.mainloop()
