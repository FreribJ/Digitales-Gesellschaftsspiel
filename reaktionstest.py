# Other Import
import time
import random

import numpy

import setup
import animations

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

zeit = [0, 0, 0, 0, 0]

def callback_zeitspeichern(switch):
    global zeit

    player = setup.player_button.index(switch)
    if zeit[player] == 0:
        zeit[player] = time.time()

#Initialzes Callback
def initialize_callback():
    for switch in setup.player_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)

#Removes Callback
def remove_callback():
    for i in setup.player_button:
        GPIO.remove_event_detect(i)


def start_reaktionstest():
    #Vorbereiten
    global zeit
    initialize_callback()
    animations.all_blink(1, random.randint(2, 7))
    zeit = [0, 0, 0, 0, 0]

    #Auf Ende Warten
    while zeit.count(0) > 0:
        time.sleep(1)
        print(zeit)

    #Gewinner berechnen
    animations.rolls(setup.player_led, 1)
    time.sleep(0.5)
    winner = zeit.index(min(zeit))
    animations.one_blink(setup.player_led[winner], 5, 0.3)

    #Ende
    remove_callback()

