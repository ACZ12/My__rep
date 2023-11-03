from ursina import *
app=Ursina()
window.color=color.orange

e1=Entity(model="sphere",texture="abred.jpg")
e1.animate_z(-15,duration=2,delay=2)
e1.animate_rotation_y(90,duration=2)














app.run()