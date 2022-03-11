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
    #Startanimation:
    print("Started")
    animations.rolls(setup.all_led, 1)

    #Spielerauswahl:
    selection.playerselection()

    #Lebenwahl:

    #Spielauswahl:

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
