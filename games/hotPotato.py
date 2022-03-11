#Other Import
import time
import random

#GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Variable Import
from control import setup
from helper import animations

actualPlayer = random.randint(0, 4)
GPIO.output(actualPlayer, 1)
timeLength = random.uniform(15, 30);
startTime = time.time()

def changePlayer():
    global actualPlayer
    GPIO.output(actualPlayer, 0)
    GPIO.remove_event_detect(setup.playerButton[actualPlayer])
    actualPlayer = random.randint(0, 4)
    GPIO.output(actualPlayer, 1)
    GPIO.add_event_detect(setup.playerButton[actualPlayer], GPIO.BOTH)

def startGame():
    GPIO.add_event_detect(setup.playerButton[actualPlayer], GPIO.BOTH)
    while time.time()-startTime <= timeLength:
        if GPIO.event_detected(actualPlayer):
            changePlayer()
    animations.blink(5)