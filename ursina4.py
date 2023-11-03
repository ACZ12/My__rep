from ursina import *
app=Ursina()


def update():
    global dx
    ball.x+=dx
    hit_info=ball.intersects()
    if hit_info.hit:
        dx*=-1
        if hit_info.entity in r:
            destroy(hit_info.entity)
        
dx=.1
r=[]
rectangle=Entity(model="cube",scale=(1,3,4),texture="white_cube",rotation=(0,0,0),position=(3,0,0),collider="box")
rectangle2=Entity(model="cube",scale=(1,3,4),texture="white_cube",rotation=(0,0,0),position=(-3,0,0),collider="box")
ball=Entity(model="sphere",texture="abred.jpg",collider="box")
r.append(rectangle)
r.append(rectangle2)












app.run()