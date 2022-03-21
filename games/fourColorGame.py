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
reihenfolge = []


#Initialzes Callback
def initializeGame():
        for switch in setup.active_button:
            GPIO.add_event_detect(switch, GPIO.RISING, bouncetime=400)

def nextRound():
    global reihenfolge
    len_reihenfolge = len(reihenfolge)

    x = random.randint(0, setup.active_player-1)
    if len_reihenfolge == 0:
        reihenfolge.append(x)
    else:
        while reihenfolge[len_reihenfolge - 1] == x:
            x = random.randint(0, setup.active_player - 1)
        reihenfolge.append(x)

    animations.one_blink(setup.active_led[x], 1, 0.5)

    # Cleanup:
    for i in setup.active_button:
        GPIO.event_detected(i)


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
    global reihenfolge

    initializeGame()
    while setup.areAllPlayerAlive():
        while True:
            abbruch = [False]
            nextRound()

            for i in reihenfolge:
                playerPressed = waitForPress()
                if playerPressed == i:
                    continue
                elif playerPressed == "zeit_limit_abgelaufen":
                    abbruch = [True, "zeit_limit_abgelaufen", i]
                    break
                else:
                    abbruch = [True, "falsch_gedrueckt", playerPressed]
                    break

            if abbruch[0]:
                if abbruch[1] == "zeit_limit_abgelaufen":
                    setup.subtractLifeFromPlayer(abbruch[2])
                    break

                if abbruch[1] == "falsch_gedrueckt":
                    setup.subtractLifeFromPlayer(abbruch[2])
                    break

            time.sleep(0.2)

        reihenfolge = []

    setup.remove_callback()