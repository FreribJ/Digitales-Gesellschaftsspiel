import time
import random

from pygame import mixer
from pygame.mixer import music

def initialize():
    mixer.init()

def playLoseSound():
    music.load("helper/Sounds/lose.wav")
    music.set_volume(1)
    music.play()

def playMenuSound():
    music.load("helper/Sounds/menuSelection.mp3")
    music.set_volume(1)
    music.play()

def playButtonPush():
    music.load("helper/Sounds/buttonpush.mp3")
    music.set_volume(0.5)
    music.play()

#tests:
def test1():
    music.load("helper/Sounds/buttonpush.mp3")
    music.set_volume(0.5)

def test2():
    music.play()

def playSound(Soundfile):
    music.load("helper/Sounds/" + Soundfile)
    music.set_volume(1)
    music.play()

def playSoundAtPosition(Soundfile, Startposition):
    music.load("helper/Sounds/" + Soundfile)
    music.set_volume(1)
    music.play(0, Startposition)

def stopSound():
    music.stop()


#test:
initialize()
playButtonPush()

#https://soundbible.com/419-Tiny-Button-Push.html
#https://www.youtube.com/watch?v=T9N0pmLI7Jw