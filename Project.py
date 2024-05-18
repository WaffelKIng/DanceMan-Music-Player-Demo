from ursina import *
import time

from ursina import *

app = Ursina()

s = Entity(model='quad', texture='pluh',scale = (14.6,8.18,10))
print(s)

titleframes = [load_texture('001.png'), load_texture('002.png'), load_texture('003.png'), load_texture('004.png'), load_texture('005.png'), load_texture('006.png'), load_texture('007.png'), load_texture('008.png'), load_texture('009.png'), load_texture('010.png'), load_texture('011.png')]
pluh = Entity(model='quad', texture=titleframes[0], scale=(2, 2), position=(2, -2.85, -1))

def update():
    update_animation()

def update_animation():
    pluh.texture = titleframes[int(time.time() * 7.5) % len(titleframes)]

print(pluh)



class MusicPlayer(Entity):
    def __init__(self):
        super().__init__()
        self.current_song_index = 0
        self.songs = ["creditsvibe.ogg", "titlescreenloop.ogg", "madness.ogg"]
        self.current_speed = 1.0
        self.paused = False
        self.looping = True

        self.sound = Audio(self.songs[self.current_song_index], loop=self.looping)
        self.sound.pitch = self.current_speed

        self.play_button = Button(text='Play/Pause', color=color.blue, on_click=self.toggle_pause)
        self.play_button.position = (-0.3, 0.3)

        self.speed_up_button = Button(text='Speed Up', color=color.green, on_click=self.speed_up)
        self.speed_up_button.position = (0.0, 0.3)

        self.slow_down_button = Button(text='Slow Down', color=color.red, on_click=self.slow_down)
        self.slow_down_button.position = (0.3, 0.3)

    def toggle_pause(self):
        if self.paused:
            self.sound.resume()
        else:
            self.sound.pause()
        self.paused = not self.paused

    def speed_up(self):
        if self.current_speed < 2.0:
            self.current_speed *= 2.0
            self.sound.pitch = self.current_speed

    def slow_down(self):
        if self.current_speed > 0.5:
            self.current_speed *= 0.5
            self.sound.pitch = self.current_speed

    def input(self, key):
        if key == 'right arrow':
            self.next_song()
        elif key == 'left arrow':
            self.previous_song()

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.songs)
        self.sound.stop()
        self.sound = Audio(self.songs[self.current_song_index], loop=self.looping)
        self.sound.pitch = self.current_speed
        if not self.paused:
            self.sound.play()

    def previous_song(self):
        self.current_song_index = (self.current_song_index - 1) % len(self.songs)
        self.sound.stop()
        self.sound = Audio(self.songs[self.current_song_index], loop=self.looping)
        self.sound.pitch = self.current_speed
        if not self.paused:
            self.sound.play()

app = Ursina()
player = MusicPlayer()
app.run()
