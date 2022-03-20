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

def reduceTime():
    global timeToPress
    timeToPress = timeToPress * 0.95
    print(timeToPress)

def startGame():
    initializeGame()

    while setup.areAllPlayerAlive():

        wrong_button_push = False
        wrong_button_push_player = 0

        while True:
            time.sleep(timeToPress)

            for i in setup.active_button:
                if not (setup.active_button.index(i) == actualPlayer):
                    if GPIO.event_detected(i):
                        wrong_button_push = True
                        wrong_button_push_player = i

            if wrong_button_push:
                setup.subtractLifeFromPlayer(setup.active_button.index(wrong_button_push_player))
                break

            if GPIO.event_detected(setup.active_button[actualPlayer]):
                reduceTime()
                changePlayer()
            else:
                setup.subtractLifeFromPlayer(actualPlayer)
                break


    for i in setup.active_button:
        GPIO.remove_event_detect(i)
