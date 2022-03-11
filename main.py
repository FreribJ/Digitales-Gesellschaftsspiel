#Other Import
import time

#GPIO Import
import reaktionstest

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Class Import
from animations import rolls
import setup



#Programm-Initialize:
setup.initialize()

#Programm-Start:
try:
    rolls(setup.all_led, 2)
    reaktionstest.start_reaktionstest()

    #Ende:
    print("Finished")
    GPIO.cleanup()

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
