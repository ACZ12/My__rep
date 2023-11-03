from ursina import *
app=Ursina()

def update():
    global speed, speed2
    cube.rotation_y=cube.rotation_y+time.dt*100
    cube.rotation_x=cube.rotation_x+time.dt*100
    cube.rotation_x=cube.rotation_x+time.dt*100
    cube.x=cube.x+time.dt*speed
    cube.y=cube.y+time.dt*speed
    if abs(cube.x)>6:
        speed*=-1
    elif abs(cube.x)>1:
        speed2*=-1



speed=5
speed2=5
cube=Entity(model="cube",rotation=(45,45,0),scale=3,color=color.green)
text=Text(text="fdsd",color=color.blue,scale=2,x=.2,y=.5)




app.run()