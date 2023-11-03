from ursina import *
app=Ursina()

def update():
    global dx
    e1.x+=dx
    if abs(e1.x)>3:
        dx=-dx




dx=.1
e1=Entity(model="circle",color=color.red,position=(0,2,0),texture="brick")
e2=Entity(model="cube",color=color.blue,position=(0,-2,0))
e2.add_script(SmoothFollow(target=e1,offset=(0,-2,0)))













app.run()