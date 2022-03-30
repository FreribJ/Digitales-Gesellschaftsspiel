from pygame import mixer
from pygame.mixer import music

soundDir = "Partyspiel/helper/Sounds/"

def initialize():
    mixer.init()

def playLoseSound():
    music.load(soundDir + "lose.wav")
    music.set_volume(1)
    music.play()

def playMenuSound():
    music.load(soundDir + "menuSelection.mp3")
    music.set_volume(1)
    music.play()

def playButtonPush():
    music.load(soundDir + "buttonpush.mp3")
    music.set_volume(0.5)
    music.play()

def playSound(Soundfile):
    music.load(soundDir + Soundfile)
    music.set_volume(1)
    music.play()

def playSoundAtPosition(Soundfile, Startposition):
    music.load(soundDir + Soundfile)
    music.set_volume(1)
    music.play(0, Startposition)

def stopSound():
    music.stop()