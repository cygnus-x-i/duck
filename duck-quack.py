import keyboard
from pygame import mixer
from os.path import abspath, dirname, join
import time


mixer.init()
paused = False
current_song_index = 0

# Define a function to be called when the hotkey is pressed
def on_hotkey():
    print("Hotkey pressed!")
    mixer.music.load('duck-quack.wav')
    mixer.music.play()
    time.sleep(3)

keyboard.add_hotkey('d', on_hotkey)

# Keep the program running to listen for hotkeys
keyboard.wait()
