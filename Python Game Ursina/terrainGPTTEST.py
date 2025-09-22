from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.models.procedural.terrain import Terrain

app = Ursina()

terrain = Terrain()
player = FirstPersonController()
player.y = 10

def input(key):
    if key == 'left mouse down' and mouse.hovered_entity == terrain:
        hit_pos = mouse.world_point
        terrain.paint(hit_pos, value=-1, radius=2)  # Lower terrain

    if key == 'right mouse down' and mouse.hovered_entity == terrain:
        hit_pos = mouse.world_point
        terrain.paint(hit_pos, value=1, radius=2)  # Raise terrain

app.run()