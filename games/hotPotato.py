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

actualPlayer = random.randint(0, setup.active_player)
GPIO.output(setup.active_led[actualPlayer], 1)
timeLength = random.uniform(15, 30);
startTime = time.time()

def changePlayer():
    global actualPlayer
    GPIO.output(setup.active_led[actualPlayer], 0)
    GPIO.remove_event_detect(setup.activeButton[actualPlayer])
    actualPlayer = random.randint(0, setup.active_player)
    GPIO.output(setup.active_led[actualPlayer], 1)
    GPIO.add_event_detect(setup.activeButton[actualPlayer], GPIO.BOTH)

def startGame():
    GPIO.add_event_detect(setup.activeButton[actualPlayer], GPIO.BOTH)
    while time.time()-startTime <= timeLength:
        if GPIO.event_detected(actualPlayer):
            changePlayer()
    animations.all_blink(5, 0.3)
    animations.one_blink(setup.active_led[actualPlayer], 5, 0.3)