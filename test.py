import time

from pygame import mixer
from pygame.mixer import music
from control import setup
# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

mixer.init()
music.load("helper/Sounds/buttonpush.mp3")


def callback(pin):
    music.play()

GPIO.add_event_detect(setup.player_button[0], GPIO.RISING, callback, 200)

time.sleep(1000)