import time
import random

from control import setup
from helper import animations, sounds

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

ran_num = 0
nummer = []

# Variablen

#Initialzes Callback
    for switch in setup.active_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)

#Nummern Speichern
def callback_zeitspeichern(switch):
    global nummer
    player = setup.active_button.index(switch)
    nummer[player] = nummer[player] + 1