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

actualPlayer = 0
timeLength = 0
startTime = 0

def initializeGame():
    global timeLength, startTime, actualPlayer
    actualPlayer = random.randint(0, setup.active_player-1)
    GPIO.output(setup.active_led[actualPlayer], 1)
    timeLength = random.uniform(15, 30);
    startTime = time.time()

def changePlayer():
    global actualPlayer
    GPIO.output(setup.active_led[actualPlayer], 0)
    GPIO.remove_event_detect(setup.active_button[actualPlayer])
    actualPlayer = random.randint(0, setup.active_player-1) #-1 da randint sonst einen zu viel macht
    GPIO.output(setup.active_led[actualPlayer], 1)
    GPIO.add_event_detect(setup.active_button[actualPlayer], GPIO.BOTH)

def startGame():
    initializeGame() #Damit die werte erst beim Start gesetzt werden

    GPIO.add_event_detect(setup.active_button[actualPlayer], GPIO.BOTH)
    while time.time()-startTime <= timeLength:
        if GPIO.event_detected(setup.active_button[actualPlayer]): #Es fehlt das: setup.active_button...
            changePlayer()
    animations.all_blink(5, 0.3)
    animations.one_blink(setup.active_led[actualPlayer], 5, 0.3)

    for i in setup.active_button:
        GPIO.remove_event_detect(i)