from ursina import *
app=Ursina()

def update():
    global x,speed
    x=x+time.dt*speed
    if abs(x)>3:
        speed*=-1
    camera.position=(x,0,20)
    
    
cubes=[]
cube=Entity(model="cube",color=color.yellow,scale=2,rotation=(20,20,0),texture="white_cube")
cubes.append(cube)

cube2=Entity(model="cube",color=color.green,rotation=(20,20,0),scale=2,texture="brick")
cubes.append(cube2)

camera.rotation_y=180
x,speed=0,1






app.run()