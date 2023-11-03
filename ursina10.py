from ursina import *
app=Ursina()

def update():
    e1.rotation_x+=time.dt*100

e1=Entity(model="cube",texture="brick",rotation=(20,20,0),color=color.red)
PointLight(z=-10,y=10)







app.run()