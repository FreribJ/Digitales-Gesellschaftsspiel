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
selected_button_arr = []
selected_led_arr = []

#Initialzes Callback
def initializeGame():
    for switch in setup.all_button:
        GPIO.add_event_detect(switch, GPIO.RISING, bouncetime=400)

def remove_callback():
    for i in setup.all_button:
        GPIO.remove_event_detect(i)

def selectRandom():
    global selected_button_arr, selected_led_arr
    selected_led_arr = []
    selected_button_arr = []
    temp_arr = []
    for i in range(selected_num):
        randNum = random.randint(0, 10-1)
        while(temp_arr.__contains__(randNum)):
            randNum = random.randint(0, selected_num - 1)
        temp_arr.append(randNum)
    temp_arr.sort()
    for i in temp_arr:
        selected_button_arr.append(setup.player_button[i])
        selected_led_arr.append(setup.player_led[i])

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
    for i in selected_button_arr: #Resetten der Pins
        GPIO.event_detected(i)
    starttime = time.time()
    while time.time()-starttime < 10 and all_pressed.count(False) > 0: #Legt die Anzahl an Sekunden Fest die gebraucht werden dürfen
        for i in selected_button_arr:
            if GPIO.event_detected(i):
                player_num = selected_button_arr.index(i)
                GPIO.output(selected_led_arr[player_num], 0)
                all_pressed[player_num] = True

def waitForContinue():
    while not GPIO.event_detected(setup.control_button[1]):
        time.sleep(0.5)
        GPIO.output(setup.control_led[1], 1)
        time.sleep(0.5)
        GPIO.output(setup.control_led[1], 0)
        if GPIO.event_detected(setup.control_button[0]):
            return "abbruch"

def startGame():
    global selected_num
    GPIO.remove_event_detect(setup.control_button[0]) #Für dieses Spiel gibt es eine andere Abbruchbedingung
    initializeGame()
    selected_num = setup.active_player - 1

    while selected_num > 0:
        if not selected_num == setup.active_player-1:
            if waitForContinue() == "abbruch":
                break
            animations.all_off()

        #Starten
        selectRandom()

        sounds.playSound("jerusalem.mp3")
        animations.rings(setup.player_led, random.randint(10, 25), 0.5)
        sounds.stopSound()
        animations.array_on(selected_led_arr)

        #Warten
        waitForAllToPress()

        time.sleep(1)
        animations.array_on(selected_led_arr)

        selected_num -= 1

    #Ende
    animations.all_off()
    remove_callback()