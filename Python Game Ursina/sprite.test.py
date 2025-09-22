from ursina import *
app = Ursina()
camera.orthographic = True
camera.fov = 1
Sprite.ppu = 16
Texture.default_filtering = None
s = Sprite('brick', filtering=False)
app.run()