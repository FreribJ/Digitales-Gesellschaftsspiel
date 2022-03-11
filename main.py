#Other Import
import time

#GPIO Import
import reaktionstest

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
    animations.rolls(setup.all_led, 1)
    reaktionstest.start_reaktionstest()

    #Ende:
    print("Finished")
    GPIO.cleanup()

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
