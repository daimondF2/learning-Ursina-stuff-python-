from ursina import *
from ursina import window
from time import pytime
app = Ursina(title = 'Beat tester')

target = Entity(model='quad', color=color.green, scale=(0.2, 0.05), y=-0.4)
notes = []
noteIndex = 0    
score = 0
scoreText = Text(text='Score: 0', position=(-0.85, 0.45), scale=2)
hold_time= 0

def spawnNote():
    note = Entity(model='quad', color=color.yellow, scale=(0.2,0.5), y = 0.5)
    notes.append(note)

def update():
    # global noteIndex
    global hold_time, score
    # if song.playing and note_index < len(beat_times):
    #     if song.time >= beat_times[note_index] - 1.0:  # spawn 1 sec early so it falls down
    #         spawn_note()
    #         note_index += 1
    for note in notes[:]:  # Use a copy of the list to avoid issues while removing
        note.y -= time.dt * 0.5

        # Auto-remove if missed
        if note.y < -1:
            print("Miss!")
            note.disable()
            notes.remove(note)
            score -= 100
            scoreText.text = f'Score: {score}'

    for note in notes:
        note.y -= time.dt * 0.5  # Moves the note down

    if held_keys['space']:
        for note in notes:
            if abs(note.y - target.y) < 0.05:
                print('Hit!')
                note.disable()
                notes.remove(note)
                score += 100
                scoreText.text = f'Score: {score}'
                break
    if held_keys['escape']:
        hold_time += time.dt  # Add delta time each frame the key is held
        if hold_time >= 2:
            print("Closing game...")
            application.quit()

# def input(key):
    # if key == 's':
    #     song.play()

# Simulate notes falling every 2 seconds
def note_spawner():
    invoke(note_spawner, delay=2)
    spawnNote()

note_spawner()
def input(key):
    if key == "left mouse down":
        scene.clear()

app.run()