import time
import random

from control import setup
from helper import animations, sounds

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

zeiten = []

#Zeiten Speichern
def callback_zeitspeichern(switch):
    zeit = time.time()
    global zeiten

    player = setup.active_button.index(switch)
    if zeiten[player] == 0:
        zeiten[player] = zeit

#Initialzes Callback
def initialize_callback():
    for switch in setup.active_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)

def startGame():
    #Vorbereiten
    global zeiten
    initialize_callback()

    while setup.areAllPlayerAlive():
        #Warten
        animations.array_on(setup.active_led)
        time.sleep(random.randint(2, 7))
        sounds.playSound("airhorn.mp3")
        time.sleep(0.4)
        animations.array_off(setup.active_led)

        #Start
        zeiten = []
        for i in range(setup.active_player):
            zeiten.append(0)

        #Auf Ende Warten
        while zeiten.count(0) > 0:
            time.sleep(1)

        #Gewinner/Verlierer berechnen
        winner = zeiten.index(min(zeiten))
        loser = zeiten.index(max(zeiten))

        setup.subtractLifeFromPlayerWithWinner(loser, winner)
        if setup.areAllPlayerAlive():
            setup.waitForContinue()

    #Ende
    setup.remove_callback()

