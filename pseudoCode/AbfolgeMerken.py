# Other Import
import time
import random

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

# Variable Import
from control import setup
from helper import animations

actualPlayer = 0
newlED = 0
bisherigeReihenfolgeLEDs = #liste, am Anfang leer


def initializeGame():
    global bisherigeReihenfolgeLEDs, newLED
    if bisherigeReihenfolgeLEDs.isEmpty:
        newLED = random.randint(0, 5)
        #zufällig gewählte LED muss aufleuchten
        GPIO.output(setup.active_led[newLED], 1)
    else
        for i xrange(0, bisherigeReihenfolgeLEDs.length):
            #led an stelle i der liste muss aufleuchten
            GPIO.output(setup.active_led[i], 1)
        newlED = random.randint(0, 5)
        GPIO.output(setup.active_led[newLED], 1)


def reihenfolgeMerkenStarten():
    global actualPlayer
    #für jede led in der liste prüfen ob sie zum richtigen zeitpunkt der reihenfolge gedrückt wurde
    for i xrange(0, bisherigeReihenfolgeLEDs.length):
        actualPlayer = i
        if GPIO.event_detected(setup.active_button[actualPlayer]):
            #gedrückte led muss leuchten
            GPIO.output(setup.active_led[actualPlayer], 1)
        else:
            setup.subtractLifeFromPlayer(von dem spieler der falsch gedrückt hat)


def startGame():
    initializeGame()
    reihenfolgeMerkenStarten()

"""
    wrong_button_push = False
    wrong_button_push_player = 0

    while time.time() - startTime <= timeLength:
        if GPIO.event_detected(setup.active_button[actualPlayer]):
            changePlayer()
        for i in setup.active_button:
            if not(setup.active_button.index(i) == actualPlayer):
                if GPIO.event_detected(i):
                    wrong_button_push = True
                    wrong_button_push_player = i
        if wrong_button_push:
            setup.subtractLifeFromPlayer(setup.active_button.index(wrong_button_push_player))
            break

    for i in setup.active_button:
        GPIO.remove_event_detect(i)

    if not wrong_button_push:
        setup.subtractLifeFromPlayer(actualPlayer)
    if setup.areAllPlayerAlive():
        startGame()
"""