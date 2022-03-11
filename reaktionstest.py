# Other Import
import time
import random

import setup
import animations

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

# Variablen


def callback_zeitspeichern(switch):
    player = setup.player_button.index(switch)
    if not zeit[player] == 0:
        zeit[player] = time.time()


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
        time.sleep(1)
    animations.rolls(setup.player_led, 1)
    for t in zeit:
        print(t)

