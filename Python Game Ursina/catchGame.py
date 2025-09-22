from ursina import *
from ursina import Ursina, held_keys, camera, duplicate, raycast, time, EditorCamera
import time as pytime
import random
app = Ursina()

'''
Casts a ray from *origin*, in *direction*, with length *distance* and returns
a HitInfo containing information about what it hit. This ray will only hit entities with a collider.

Use optional *traverse_target* to only be able to hit a specific entity and its children/descendants.
Use optional *ignore* list to ignore certain entities.
Setting debug to True will draw the line on screen.

Example where we only move if a wall is not hit:
'''
wall_left = Entity(model='cube', collider='box', scale_y=3, origin_y=-.5, color=color.azure, x=-4)
wall_right = duplicate(wall_left, x=4)
camera.y = 2
#ground
ground = Entity(model='plane', scale = 10, texture='white_cube', collider='box', texture_scale=(10,10), y=0)
falling_Cubes = []
class Player(Entity):

    def update(self):
        self.direction = Vec3(
            self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()  # get the direction we're trying to walk in.

        origin = self.world_position + (self.up*.5) # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
        hit_info = raycast(origin , self.direction, ignore=(self,), distance=.5, debug=False)
        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt
player = Player(model='cube', origin_y=-.5, color=color.orange)

def spawnFallingCube():
    x = random.uniform(-3, 3)  # random x between walls
    z = random.uniform(-1, 1)  # optional: slight random z variation
    new_cube = FallingCube(position=(x, 5, -.5))
    falling_Cubes.append(new_cube)
# fallign objects
class FallingCube(Entity):
    def __init__(self, position=(0,5, 0), fall_delay=2, **kwargs):
        super().__init__(model='sphere', color=color.random_color(), position = position, collider='box',**kwargs)
        self.gravity = 2
        self.grounded = False
        self.fall_delay = fall_delay
        self.spawn_time = pytime.time()
    def update(self): #check if on ground or below level
        currentTime = pytime.time()
        if currentTime - self.spawn_time < self.fall_delay:
            return
        if not self.grounded:
            self.y -= self.gravity * time.dt
            
            #check if cube touches ground
            hit= self.intersects()
            if hit.hit:
                destroy(self)
                spawnFallingCube()
            # if self.intersects().hit:
            #     self.grounded = True
            #     self.y= self.intersects().entity.world_y + 0.5 #adjusts to sit on surface
            if self.intersects(player).hit:
                destroy(self)
                spawnFallingCube()
class score():
    def update():
        global score



for _ in range(3):
    spawnFallingCube()

#spawn 3 falling cubes 



app.run()