import tkinter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
canvas=tkinter.Canvas(height=400,width=400)
canvas.pack()

def vonal(e):
 x=e.x
 y=e.y
 canvas.create_line(200,200,x,y,fill='red')
 if e.x<200 and e.y<200:
  canvas.create_line(200,200,x,y,fill='red')
 elif e.x>200 and e.y<200:
  canvas.create_line(200,200,x,y,fill='green')
 elif e.x<200 and e.y>200:
  canvas.create_line(200,200,x,y,fill='blue')
 else: canvas.create_line(200,200,x,y,fill='yellow')

 canvas.bind('<Button-1>',vonal)
