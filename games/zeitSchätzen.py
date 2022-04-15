import random
import time

from control import setup
from helper import animations

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

zeiten = []
zeitZuSchaetzen = 10 #Zu schätzende Zeit in Sekunden

#Zeiten Speichern
def callback_zeitspeichern(switch):
    zeit = time.time()
    global zeiten

    player = setup.active_button.index(switch)
    if zeiten[player] == 0:
        zeiten[player] = zeit

#Initialzes Callback
def initializeGame():
    for switch in setup.active_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)

def startGame():
    global zeiten
    initializeGame()

    while setup.areAllPlayerAlive():
        #Setup
        zeitZuSchaetzen = random.randint(2, min(10, setup.max_player))
        animations.one_blink(setup.player_led[zeitZuSchaetzen-1], 1, 2)
        time.sleep(1)

        # Start
        animations.all_blink(1, 2)

        zeiten = []
        for i in range(setup.active_player):
            zeiten.append(0)

        acutalZeitZuSchaetzen = time.time() + zeitZuSchaetzen

        # Auf Ende Warten
        while zeiten.count(0) > 0:
            time.sleep(1)

        closest_time = abs(zeiten[0] - acutalZeitZuSchaetzen)
        closest_player = 0
        farest_time = abs(zeiten[0] - acutalZeitZuSchaetzen)
        farest_player = 0
        for i in range(setup.active_player-1):
            p_time = abs(zeiten[i+1] - acutalZeitZuSchaetzen)
            if p_time < closest_time:
                closest_player = i + 1
                closest_time = p_time
            elif p_time > farest_time:
                farest_player = i + 1
                farest_time = p_time

        setup.subtractLifeFromPlayerWithWinner(farest_player, closest_player)
        if setup.areAllPlayerAlive():
            setup.waitForContinue()

    setup.remove_callback()

