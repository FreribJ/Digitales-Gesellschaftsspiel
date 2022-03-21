import time
import random

from control import setup
from helper import animations

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

ran_num = 0
nummer = []
i = 0

#Nummern Speichern
def callback_zeitspeichern(switch):
    global nummer, i
    i=i+1;
    player = setup.active_button.index(switch)
    nummer [player] = max(i, ran_num) - min(i, ran_num)

#Initialzes Callback
def initialize_callback():
    for switch in setup.active_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)

def startGame():
    #Vorbereiten
    global nummer, ran_num
    initialize_callback()

    while setup.areAllPlayerAlive():
        #Warten
        animations.all_blink(1, random.randint(2, 5))

        #Start
        ran_num =  random.randint(9, 21)
        time.sleep(1)
        nummer = []
        for i in range(setup.active_player):
            nummer.append(0)

        # Blinken
        for t in range(ran_num):
            sleepTime = random.randint(150, 450)
            animations.one_blink(setup.all_led[random.randint(0, setup.max_player-1)], 1, sleepTime/1000)
            time.sleep(sleepTime/1000)


        #Auf Ende Warten
        time.sleep(8)

        #Debug:
        print("Zahl: ", ran_num)
        print("Player: ", nummer)

        #Gewinner/Verlierer berechnen
        winner = nummer.index(min(nummer))
        loser = nummer.index(max(nummer))

        setup.subtractLifeFromPlayerWithWinner(loser, winner)

    #Ende
    setup.remove_callback()