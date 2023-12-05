import tkinter

from random import *

canvas = tkinter.Canvas()

canvas.pack()



def negyzet(event):

	x = randrange(300)

	y = randrange(250)

	canvas.create_rectangle(x, y, x+50, y+50)

def kor(event):

	x = randrange(300)

	y = randrange(250)

	canvas.create_oval(x, y, x+50, y+50)

def felfele_nyil(event):

	x = randrange(300)

	y = randrange(250)

	canvas.create_line(x-10, y+20, x, y, x+10, y+20)

	canvas.create_line(x, y, x, y+40)

def lefele_nyil(event):

	x = randrange(300)

	y = randrange(250)

	canvas.create_line(x-10, y-20, x, y, x+10, y-20)

	canvas.create_line(x, y, x, y-40)

def jobbra_nyil(event):

	x = randrange(300)

	y = randrange(250)

	canvas.create_line(x-20, y-10, x, y, x-20, y+10)

	canvas.create_line(x, y, x-40, y)

def balra_nyil(event):

	x = randrange(300)

	y = randrange(250)

	canvas.create_line(x-20, y-10, x-40, y, x-20, y+10)

	canvas.create_line(x, y, x-40, y)

	

canvas.bind_all('n', negyzet)

canvas.bind_all('k', kor)

canvas.bind_all('<Up>', felfele_nyil)

canvas.bind_all('<Down>', lefele_nyil)

canvas.bind_all('<Right>', jobbra_nyil)

canvas.bind_all('<Left>', balra_nyil)

canvas.mainloop()