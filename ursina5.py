from ursina import *
app=Ursina()





class Player(Entity):
    def __init__(self, x, speed):
        super().__init__()
        self.model="cube"
        self.color=color.red
        scale_y=2
        self.x=x
        self.speed=speed
        
    def update(self):
        self.x+=held_keys["right arrow"]*time.dt*self.speed
        self.x-=held_keys["left arrow"]*time.dt*self.speed
    
    def input(self,key):
        if key=="space":
            self.color=color.random_color()
        if key=="r":
            self.rotation_z+=time.dt*500
        if key=="0":
            Player.reset(self)
    def reset(self):
        self.color=color.red
        self.rotation_z=0
        self.x=x
    
    
    
x=-2
speed=10
player=Player(x,speed)


Entity(model="cube",texture="brick")




PointLight(x=-5,y=-5,z=-5,)
PointLight(x=5,y=5,z=5,)
app.run()