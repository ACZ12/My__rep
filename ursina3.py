from ursina import *
app=Ursina()

def update():
    #global y
    for e in cubes:
        #y+=0.1
        if held_keys["r"]:
            e.rotation_y=e.rotation_y+time.dt*100
            #camera.position=(0,0,y)



#y=0
cubes=[]

cube=Entity(model="cube",color=color.yellow,scale=1,rotation=(20,20,0),texture="white_cube",position=(4,0,0))
cubes.append(cube)
cube2=Entity(model="cube",color=color.red,scale=1,rotation=(20,20,0),texture="brick",position=(2,0,0))
cubes.append(cube2)
cube3=Entity(model="cube",color=color.blue,scale=1,rotation=(20,20,0),texture="radial_gradient",position=(0,0,0))
cubes.append(cube3)
cube4=Entity(model="cube",color=color.green,scale=1,rotation=(20,20,0),texture="HMD_Doh..png",position=(-2,0,0))
cubes.append(cube4)
cube5=Entity(model="sphere",color=color.pink,scale=1,rotation=(20,20,0),texture="sel.png",position=(-4,0,0))
cubes.append(cube5)







app.run()