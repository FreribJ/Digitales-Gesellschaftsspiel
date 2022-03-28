import random
import time

from control import setup
from helper import animations

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Variablen
next_player = 0
counter = 1
passing_number = 0


#Initialzes Callback
def initializeGame():
        for switch in setup.active_button:
            GPIO.add_event_detect(switch, GPIO.RISING, bouncetime=400)

def setNext():
    global counter, next_player
    counter += 1

    while beinhaltetPassingNumber():
        counter += 1

    next_player = next_player + counter % setup.active_player - 1

    # Cleanup:
    for i in setup.active_button:
        GPIO.event_detected(i)

def beinhaltetPassingNumber():
    if counter % passing_number == 0:
        return True
    if str(counter).__contains__(str(passing_number)):
        return True
    return False

def waitForPress():
    starttime = time.time()
    while time.time()-starttime < 5: #Legt die Anzahl an Sekunden Fest die gebraucht werden dürfen
        for i in setup.active_button:
            if GPIO.event_detected(i):
                player_num = setup.active_button.index(i)
                animations.one_blink(setup.active_led[player_num], 1, 0.2)
                return player_num
    return "zeit_limit_abgelaufen"


def startGame():
    global next_player, passing_number, counter

    initializeGame()
    while setup.areAllPlayerAlive():
        next_player = 0
        counter = 1
        passing_number = 7 #evtl. durch random.randint(2, 10) ersetzbar-> aber Anzeigen!
        GPIO.output(setup.active_led[next_player], 1)

        while True:
            playerPressed = waitForPress()
            if playerPressed == next_player:
                continue
            elif playerPressed == "zeit_limit_abgelaufen":
                setup.subtractLifeFromPlayer(next_player)
                break
            else:
                setup.subtractLifeFromPlayer(playerPressed)
                break

            setNext()


    setup.remove_callback()