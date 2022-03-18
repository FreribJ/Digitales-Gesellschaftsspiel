# Other Import
import random
import time

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

# Variable Import
from control import setup

actualPlayer = 0
timeToPress = 0

def initializeGame():
    global actualPlayer, timeToPress
    actualPlayer = random.randint(0, setup.active_player - 1)
    timeToPress = 2
    GPIO.output(setup.active_led[actualPlayer], 1)
    for i in setup.active_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=200)


def changePlayer():
    global actualPlayer
    GPIO.output(setup.active_led[actualPlayer], 0)
    x = random.randint(0, setup.active_player - 1)
    while x == actualPlayer:
        x = random.randint(0, setup.active_player - 1)
    actualPlayer = x
    GPIO.output(setup.active_led[actualPlayer], 1)


def startGame():
    while setup.areAllPlayerAlive():

        initializeGame()
        start_time = time.time()
        time_over = False

        while not time_over:
            if start_time + timeToPress > time.time():
                time_over = True
                break
            if GPIO.event_detected(setup.active_button[actualPlayer]):
                changePlayer()
                break
            for i in setup.active_button:
                if not (setup.active_button.index(i) == actualPlayer):
                    if GPIO.event_detected(i):
                        wrong_button_push = True
                        wrong_button_push_player = i
            if wrong_button_push:
                setup.subtractLifeFromPlayer(setup.active_button.index(wrong_button_push_player))
                break

        if time_over:
            setup.subtractLifeFromPlayer(actualPlayer)

        for i in setup.active_button:
            GPIO.remove_event_detect(i)
