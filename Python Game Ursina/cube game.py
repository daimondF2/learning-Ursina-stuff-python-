from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

# Player and sky
player = FirstPersonController()
Sky()

# List to track blocks
boxes = []

# Build flat platform of blocks (20x20 at Y=0)
for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube', position=(j, 0, i), texture='grass.png', parent=scene, origin_y=0.5, collider='box')  # <- allows player to walk on it)
        boxes.append(box)

    
#settings
#toggle_outline = Checkbox(text="Show Block Outlines", default=True)
sensitivity_slider = Slider(min=0.5, max=3, default=1, step=0.1)
def quit():
    application.quit()

def close_settings():
    settings_Panel.enabled = False
    mouse.locked = True
    mouse.visible = False
    player.enabled = True

settings_Panel = WindowPanel(title='Settings', content=(
                            Text("Mouse Sensitivity "), 
                            sensitivity_slider,
                            Button(text='Close Settings', color=color.azure, on_click=close_settings),
                            Button(text='exit game', color=color.red, on_click=quit),
                            #Button(text=')
                            ),
                            position=window.center,
                            enabled=False)


def updateSensitivity():
    if settings_Panel.enabled:
        player.mouse_sensitivity = Vec2(sensitivity_slider.value, sensitivity_slider.value)


def input(key):
    if key == 'tab':
        settings_Panel.enabled = not settings_Panel.enabled
        
        # If opening settings
        if settings_Panel.enabled:
            mouse.locked = False
            mouse.visible = True
            player.enabled = False  # disable movement
        else:
            mouse.locked = True
            mouse.visible = False
            player.enabled = True   # resume movement
    # Mouse build/destroy blocks
    if not settings_Panel.enabled:
        for box in boxes:
            if box.hovered:
                if key == 'left mouse down':
                    new = Button(color=color.white, model='cube', position=box.position + mouse.normal, texture='grass.png', parent=scene, origin_y=0.5, collider='box')
                    boxes.append(new)
                elif key == 'right mouse down':
                    boxes.remove(box)
                    destroy(box)



mouse.locked = True
mouse.visible = False
app.run()