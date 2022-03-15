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
timeLength = 0
startTime = 0


def initializeGame():
    global timeLength, startTime, actualPlayer
    actualPlayer = random.randint(0, setup.active_player - 1)
    GPIO.output(setup.active_led[actualPlayer], 1)
    timeLength = random.uniform(15, 30);
    startTime = time.time()
    for i in setup.active_button:
        GPIO.add_event_detect(i, GPIO.BOTH)


def changePlayer():
    global actualPlayer
    GPIO.output(setup.active_led[actualPlayer], 0)
    x = random.randint(0, setup.active_player - 1)
    while x == actualPlayer:
        x = random.randint(0, setup.active_player - 1)
    actualPlayer = x
    GPIO.output(setup.active_led[actualPlayer], 1)


def startGame():
    initializeGame()
    wrong_button_push = False
    wrong_button_push_player = 0

    while time.time() - startTime <= timeLength:
        if GPIO.event_detected(setup.active_button[actualPlayer]):
            changePlayer()
        for i in setup.active_button:
            if GPIO.event_detected(i) and not(i == actualPlayer):
                setup.subtractLifeFromPlayer(actualPlayer)
                wrong_button_push = True
                wrong_button_push_player = i
        if wrong_button_push:
            setup.subtractLifeFromPlayer(wrong_button_push_player)
            break

    for i in setup.active_button:
        GPIO.remove_event_detect(i)

    if not wrong_button_push:
        setup.subtractLifeFromPlayer(actualPlayer)
    if setup.areAllPlayerAlive():
        startGame()
