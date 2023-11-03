import tkinter,random
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()

def animacio():
    global x,y,szamjegy0,szamjegy1
    szam=random.randint(0,1)
    if szam==0:
        szin='blue'
        szamjegy0=szamjegy0+1
    else:
        szin='green'
        szamjegy1=szamjegy1+1
    canvas.create_text(x,y,text=szam,fill=szin)
    x=x+10
    if x>80:
        x=10
        y=y+10
    if y<390 and stop==0:
        canvas.after(10,animacio)
    if y>=390:
        print('0-k száma:',szamjegy0)
        print('1-esek száma:',szamjegy1)

def s_betu_megnyomasa(event):
    global stop
    if stop==1:
        stop=0
        canvas.after(100,animacio)
    else:
         stop=1

x=10
y=10
szamjegy0=0
szamjegy1=0
stop=0
canvas.create_text(300,350,text='Nyomd meg az s-t a megállításhoz')
canvas.bind_all('s',s_betu_megnyomasa)
animacio()
