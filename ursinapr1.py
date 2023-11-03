
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.exit_button.visible = False
window.fps_counter_enabled = False

class Level1Class(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=scene)
        self.player = FirstPersonController()
        self.player.position = (0, 1, 0)  # Adjust player's initial position
        self.blocks = []

    def environment(self):
        Sky(texture="sky_default")
        self.ground = Entity(
            model="plane",
            texture="grass",
            collider="box",
            scale=Vec3(100, 1, 100))

        self.wall1 = Entity(
            parent=scene,
            scale=Vec3(1, 1, 1),  # Adjusted scale to Vec3
            position=Vec3(20, 0, 0),
            rotation=Vec3(0, 270, 0),
            model="house.glb",
            texture="brick",
            collider="box")
        
        self.ball = Entity(
            parent=scene,
            scale=Vec3(1, 1, 1),  # Adjusted scale to Vec3
            position=Vec3(2, 2, 0),
            rotation=Vec3(0, 270, 0),
            model="ball.glb",
            texture="brick",
            collider="mesh")


        self.wall2=duplicate(self.wall1,position=Vec3(0,0,20),rotation=Vec3(0,0,0))

def windowChoice(choice):
    if choice == "level_1":
        level_1 = Level1Class()
        level_1.environment()

windowChoice("level_1")  # Call the function with the argument


app.run()