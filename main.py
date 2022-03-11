import time

from helper import animations
from control import setup, selection
from games import reaktionstest

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


#Programm-Initialize:
setup.initialize()

#Programm-Start:
try:
    menu_level = 0
    #Startanimation:
    print("Started")
    animations.rolls(setup.all_led, 3)

    while True:
        try:
            #Spielerauswahl:
            if menu_level == 0:
                GPIO.output(setup.control_led[0], 1)
                selection.playerselection()
                animations.rolls(setup.all_led, 1)
                GPIO.output(setup.control_led[0], 0)
                menu_level = 1

            #Lebenwahl:
            if menu_level == 1:
                GPIO.output(setup.control_led[1], 1)
                time.sleep(2)
                animations.rolls(setup.all_led, 1)
                GPIO.output(setup.control_led[1], 0)
                menu_level = 2

            #Spielauswahl:
            if menu_level == 2:
                GPIO.output(setup.control_led[2], 1)
                time.sleep(q)
                animations.rolls(setup.all_led, 1)
                GPIO.output(setup.control_led[2], 0)

        except TabError:
            if menu_level == 0:
                break
            else:
                menu_level -= 1


    #Spielstart
    while True:
        reaktionstest.start_reaktionstest()

    #Ende:
    animations.rolls(setup.all_led, 1)
    print("Finished")
    GPIO.cleanup()

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
