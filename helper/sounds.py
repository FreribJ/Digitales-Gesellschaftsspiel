import time
import random

from pygame import mixer
from pygame.mixer import music

def initialize():
    mixer.init()

def playLoseSound():
    music.load("Sounds/lose.wav")
    music.set_volume(1)
    music.play()

def playMenuSound():
    music.load("Sounds/menuSelection.mp3")
    music.set_volume(1)
    music.play()

def playButtonPush():
    music.load("Sounds/buttonpush.mp3")
    music.set_volume(0.5)
    music.play()

def playSound(Soundfile):
    music.load("Sounds/" + Soundfile)
    music.set_volume(1)
    music.play()

def playSoundAtPosition(Soundfile, Startposition):
    music.load("Sounds/" + Soundfile)
    music.set_volume(1)
    music.play(0, Startposition)

def stopSound():
    music.stop()


#test:


#https://soundbible.com/419-Tiny-Button-Push.html
#https://www.youtube.com/watch?v=T9N0pmLI7Jw