import random
import time

from control import setup
from helper import animations

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Variablen
reihenfolge = []


#Initialzes Callback
def initializeGame():
        for switch in setup.active_button:
            GPIO.add_event_detect(switch, GPIO.RISING, 400)

def nextRound():
    global reihenfolge
    len_reihenfolge = len(reihenfolge)

    x = random.randint(0, setup.active_player-1)
    if len_reihenfolge == 0:
        reihenfolge.append(x)
    else:
        while reihenfolge[len_reihenfolge - 1] == x:
            x = random.randint(0, setup.active_player - 1)
        reihenfolge.append(x)

    animations.one_blink(setup.active_led[x], 1, 1)


def waitForPress():
    #Cleanup:
    for i in setup.active_button:
        GPIO.event_detected(i)

    while True:
        for i in setup.active_button:
            if GPIO.event_detected(i):
                return setup.active_button.index(i)


def start_game():
    initializeGame()
    while setup.areAllPlayerAlive():
        while True:
            abbruch = False
            nextRound()
            for i in reihenfolge:
                playerPressed = waitForPress() #ForHowLong einfügen
                if playerPressed == i:
                    continue
                else:
                    abbruch = True
                    break

            if abbruch:
                setup.subtractLifeFromPlayer(i)
                break

            time.sleep(1)