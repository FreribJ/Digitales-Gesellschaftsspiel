#Other Import

#GPIO Import
from games import reaktionstest

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Class Import
import animations
import setup



#Programm-Initialize:
setup.initialize()

#Programm-Start:
try:
    #Startanimation:
    animations.rolls(setup.all_led, 1)

    #Spielerauswahl:

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
