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
count_pressed = 0

def callback_zeitspeichern(switch):
    global zeit
    global count_pressed

    player = setup.player_button.index(switch)
    if zeit[player] == 0:
        zeit[player] = time.time()
        count_pressed += 1


def initialize_callback():
    for switch in setup.player_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)

def remove_callback():
    for i in setup.player_button:
        GPIO.remove_event_detect(i)


def start_reaktionstest():
    #Vorbereiten
    global zeit
    global count_pressed
    initialize_callback()
    animations.all_blink(1, random.randint(2, 7))
    count_pressed = 0
    zeit = [0, 0, 0, 0, 0]

    #Auf Ende Warten
    while count_pressed < len(setup.player_button):
        time.sleep(1)

    #Gewinner berechnen
    animations.rolls(setup.player_led, 1)
    time.sleep(0.5)
    winner = zeit.index(min(zeit))

    animations.one_blink(setup.player_led[winner], 5, 0.3)

