import time
import random

from control import setup
from helper import animations

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

zeit = []
for i in range(setup.active_player):
    zeit.append(0)

#Zeiten Speichern
def callback_zeitspeichern(switch):
    global zeit

    player = setup.active_button.index(switch)
    if zeit[player] == 0:
        zeit[player] = time.time()

#Initialzes Callback
def initialize_callback():
    for switch in setup.active_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)

#Removes Callback
def remove_callback():
    for i in setup.active_button:
        GPIO.remove_event_detect(i)


def start_reaktionstest():
    #Vorbereiten
    global zeit
    initialize_callback()

    while setup.areAllPlayerAlive():
        animations.all_blink(1, random.randint(2, 7))

        zeit = []
        for i in range(setup.active_player):
            zeit.append(0)

        #Auf Ende Warten
        while zeit.count(0) > 0:
            time.sleep(1)

        #Gewinner/Verlierer berechnen
        winner = zeit.index(min(zeit))
        loser = zeit.index(max(zeit))

        setup.subtractLifeFromPlayer(loser, winner)

    #Ende
    remove_callback()

