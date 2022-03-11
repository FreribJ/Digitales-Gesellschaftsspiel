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
    GPIO.output(setup.control_led[0], 1)
    selection.playerselection()
    animations.rolls(setup.all_led, 1)
    GPIO.output(setup.control_led[0], 0)

    #Lebenwahl:
    GPIO.output(setup.control_led[1], 1)

    animations.rolls(setup.all_led, 1)
    GPIO.output(setup.control_led[1], 0)

    #Spielauswahl:
    GPIO.output(setup.control_led[2], 1)

    animations.rolls(setup.all_led, 1)
    GPIO.output(setup.control_led[2], 0)

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
