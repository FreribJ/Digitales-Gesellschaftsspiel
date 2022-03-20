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
    global timeToPress
    initializeGame()

    while setup.areAllPlayerAlive():

        for i in setup.active_button:
            GPIO.event_detected(i)

        timeToPress = 2
        changePlayer()

        while True:
            wrong_button_push = False
            wrong_button_push_players = []

            #Start bzw. Wartezeit
            time.sleep(timeToPress)

            #Auf Falschdruck prüfen
            for i in setup.active_button:
                if not (setup.active_button.index(i) == actualPlayer):
                    if GPIO.event_detected(i):
                        wrong_button_push = True
                        wrong_button_push_players.append(setup.active_button.index(i))
                        break

            if wrong_button_push:
                setup.subtractLifeFromPlayerArray(wrong_button_push_players)
                break

            #Auf Richtigen knopfdruck prüfen
            if GPIO.event_detected(setup.active_button[actualPlayer]):
                reduceTime()
                changePlayer()
            else:
                setup.subtractLifeFromPlayer(actualPlayer)
                break


    for i in setup.active_button:
        GPIO.remove_event_detect(i)
