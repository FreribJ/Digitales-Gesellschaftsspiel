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
from helper import sounds

actualPlayer = 0
timeLength = 0
startTime = 0


def initializeGame():
    global timeLength, startTime, actualPlayer
    actualPlayer = random.randint(0, setup.active_player - 1)
    GPIO.output(setup.active_led[actualPlayer], 1)
    timeLength = random.randint(15, 30)
    startTime = time.time()
    for i in setup.active_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=200)


def changePlayer():
    global actualPlayer
    print("player Changed from: ", actualPlayer)
    GPIO.output(setup.active_led[actualPlayer], 0)
    x = random.randint(0, setup.active_player - 1)
    while x == actualPlayer:
        x = random.randint(0, setup.active_player - 1)
    actualPlayer = x
    GPIO.output(setup.active_led[actualPlayer], 1)
    print("player Changed to: ", actualPlayer)
    print("")


def startGame():
    initializeGame()
    wrong_button_push = False
    wrong_button_push_player = 0

    sounds.playSoundAtPosition("bombticking.mp3", 30.6-timeLength)
    while time.time() - startTime <= timeLength:
        if GPIO.event_detected(setup.active_button[actualPlayer]):
            changePlayer()
        for i in setup.active_button:
            if not(i == setup.active_button[actualPlayer]):
                if GPIO.event_detected(i):
                    wrong_button_push = True
                    wrong_button_push_player = i
                    break
        if wrong_button_push:
            setup.subtractLifeFromPlayer(setup.active_button.index(wrong_button_push_player))
            sounds.stopSound()
            break

    print("Spiel vorbei")

    for i in setup.active_button:
        GPIO.remove_event_detect(i)

    if not wrong_button_push:
        setup.subtractLifeFromPlayer(actualPlayer)
    if setup.areAllPlayerAlive():
        startGame()
