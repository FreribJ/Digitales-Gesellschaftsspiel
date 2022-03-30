import time
import random

from control import setup
from helper import animations, sounds

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

selected_num = 0
selected_arr = []

#Initialzes Callback
def initializeGame():
        for switch in setup.all_button:
            GPIO.add_event_detect(switch, GPIO.RISING, bouncetime=400)

def selectRandom():
    global selected_arr
    temp_arr = []
    for i in range(selected_num):
        randNum = random.randint(0, 10-1)
        while(temp_arr.__contains__(randNum)):
            randNum = random.randint(0, selected_num - 1)
        temp_arr.append(randNum)
    temp_arr.sort()
    for i in temp_arr:
        selected_arr.append(setup.all_button[i])

def waitForPress():
    starttime = time.time()
    while time.time()-starttime < 5: #Legt die Anzahl an Sekunden Fest die gebraucht werden dürfen
        for i in setup.active_button:
            if GPIO.event_detected(i):
                player_num = setup.active_button.index(i)
                sounds.playButtonPush()
                animations.one_blink(setup.active_led[player_num], 1, 0.2)
                return player_num
    return "zeit_limit_abgelaufen"

def waitForAllToPress():
    all_pressed = []
    for i in range(selected_num):
        all_pressed.append(False)
    starttime = time.time()
    while time.time()-starttime < 10 or all_pressed.count(False) == 0: #Legt die Anzahl an Sekunden Fest die gebraucht werden dürfen
        for i in selected_arr:
            if GPIO.event_detected(i):
                GPIO.output(i, 0)
                player_num = selected_arr.index(i)
                all_pressed[player_num] = True

def startGame():
    global selected_num
    initializeGame()
    selected_num = setup.active_player - 1

    while setup.areAllPlayerAlive():
        #Starten
        selectRandom()

        animations.array_on(selected_arr)
        sounds.playSound("jerusalem.mp3")
        time.sleep(random.randint(15, 30))
        sounds.stopSound()

        #Warten
        waitForAllToPress()

        time.sleep(1)

        #Leben abziehen
        animations.array_on(setup.active_led)
        setup.subtractLifeFromPlayer(waitForPress())

        selected_num -= 1
