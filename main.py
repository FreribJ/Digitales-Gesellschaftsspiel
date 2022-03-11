import time

from helper import animations
from control import setup, selection
from games import reaktionstest

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

def callback_back(switch):
    raise TabError

#Programm-Initialize:
setup.initialize()

#Programm-Start:
try:
    #Startanimation:
    print("Started")
    animations.rolls(setup.all_led, 1)

    menu_level = 0
    while True:
        #Spielerauswahl:
        if menu_level == 0:
            print("Spielerauswahl")
            GPIO.output(setup.control_led[0], 1)
            next_level = selection.player_selection()
            animations.rolls(setup.player_led, 1)
            GPIO.output(setup.control_led[0], 0)
            if next_level:
                menu_level = 1
            else:
                break

        #Lebenwahl:
        if menu_level == 1:
            print("Lebenauswahl")
            GPIO.output(setup.control_led[1], 1)
            next_level = selection.life_selection()
            animations.rolls(setup.player_led, 1)
            GPIO.output(setup.control_led[1], 0)
            if next_level:
                menu_level = 2
            else:
                menu_level = 0

        #Spielauswahl:
        if menu_level == 2:
            print("Spielauswahl")
            GPIO.output(setup.control_led[2], 1)
            next_level = selection.game_selection()
            animations.rolls(setup.player_led, 1)
            GPIO.output(setup.control_led[2], 0)
            if next_level:
                menu_level = 2
            else:
                menu_level = 0

    #Ende:
    animations.rolls(setup.all_led, 1)
    print("Finished")
    GPIO.cleanup()

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
