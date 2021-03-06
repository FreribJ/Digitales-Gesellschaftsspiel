import random
import time

from control import setup
from helper import animations, sounds

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Variablen
counter = 1
next_player = 0
skiped_player = 0
started_player = 0
passing_number = 7 #Nummer einstellbar

def setNext():
    global counter, next_player, started_player, skiped_player
    skiped_player = 0
    def beinhaltetPassingNumber():
        if counter % passing_number == 0:
            return True
        if str(counter).__contains__(str(passing_number)):
            return True
        return False

    counter += 1

    while beinhaltetPassingNumber():
        counter += 1
        skiped_player += 1

    next_player = (counter-1+started_player) % setup.active_player


def waitForPress():
    starttime = time.time()
    maxtime = 10 + (skiped_player * 2)
    while time.time()-starttime < maxtime: #Legt die Anzahl an Sekunden Fest die gebraucht werden dürfen
        for i in setup.active_button:
            if GPIO.event_detected(i):
                player_num = setup.active_button.index(i)
                sounds.playButtonPush()
                animations.one_blink(setup.active_led[player_num], 1, 0.2)
                return player_num
    return "zeit_limit_abgelaufen"


def startGame():
    global next_player, passing_number, counter, started_player, skiped_player

    setup.add_eventDetect(400)
    while setup.areAllPlayerAlive():
        started_player = random.randint(0, setup.active_player - 1) #Zufälliger Startspieler
        next_player = started_player
        counter = 1
        skiped_player = 0
        #passing_number = evtl. durch random.randint(2, 10) ersetzbar-> aber Anzeigen!
        GPIO.output(setup.active_led[next_player], 1) #Startender Spieler anzeigen

        while True:
            playerPressed = waitForPress()
            if playerPressed == next_player:
                setNext()
            elif playerPressed == "zeit_limit_abgelaufen":
                setup.subtractLifeFromPlayer(next_player)
                break
            else:
                setup.subtractLifeFromPlayer(playerPressed)
                break

        if setup.areAllPlayerAlive():
            setup.waitForContinue()

        # Cleanup:
        setup.reset_eventDetect()

    setup.remove_eventDetect()