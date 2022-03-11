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
        count_pressed = count_pressed + 1


def initialize_callback():
    for switch in setup.player_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)

def remove_callback():
    for i in setup.player_button:
        GPIO.remove_event_detect(i)


def start_reaktionstest():
    global zeit
    global count_pressed
    initialize_callback()
    animations.blink(random.randint(2, 7))
    count_pressed = 0
    zeit = [0, 0, 0, 0, 0]
    while count_pressed < len(setup.all_button):
        print(zeit)
        print(count_pressed)
        time.sleep(1)


    animations.rolls(setup.player_led, 1)

    minZeit = numpy.minimum(zeit)

    print(minZeit)
    print(zeit.index(minZeit))

