# Other Import
import math
import random
import time

# GPIO Import
from control.setup import pi, event_detector

# Variable Import
from control import setup
from helper import sounds

actualPlayer = 0
timeToPress = 0
timesPressed = 0

def changePlayer():
    global actualPlayer
    pi.write(setup.active_led[actualPlayer], 0)
    x = random.randint(0, setup.active_player - 1)
    while x == actualPlayer:
        x = random.randint(0, setup.active_player - 1)
    actualPlayer = x
    pi.write(setup.active_led[actualPlayer], 1)

def reduceTime():
    global timeToPress, timesPressed
    timesPressed += 1
    timeToPress = 2 - 0.35 * math.log(timesPressed) #alte Berechnung: timeToPress * 0.96 #Faktor um die Zeit kanpper wird

#originally from jan, but fixed
def startGame():
    global timeToPress, timesPressed
    setup.add_eventDetect(200)

    while setup.areAllPlayerAlive():

        timesPressed = 0
        reduceTime()
        changePlayer()

        while True:
            wrong_button_push = False
            wrong_button_push_players = []

            #Start bzw. Wartezeit
            time.sleep(timeToPress)
            #Auf Falschdruck prüfen
            for i in setup.active_button:
                if not (setup.active_button.index(i) == actualPlayer):
                    if event_detector.event_detected(i):
                        wrong_button_push = True
                        wrong_button_push_players.append(setup.active_button.index(i))

            if wrong_button_push:
                setup.subtractLifeFromPlayerArray(wrong_button_push_players)
                break

            #Auf Richtigen knopfdruck prüfen
            if event_detector.event_detected(setup.active_button[actualPlayer]):
                sounds.playPingPong()
                reduceTime()
                changePlayer()
            else:
                setup.subtractLifeFromPlayer(actualPlayer)
                break

        if setup.areAllPlayerAlive():
            setup.waitForContinue()
            time.sleep(2)
        setup.reset_eventDetect()


    setup.remove_eventDetect()
