#GPIO Import
import numpy as numpy

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Other Import
import time

#Class Import
from animations import *


#Setup:
GPIO.setmode(GPIO.BCM)

controll_led = [14, 15, 18]
player_led = [23, 24, 25, 8, 7]
all_led = numpy.concatenate(controll_led, player_led)   #controll_led [14, 15, 18, 23, 24, 25, 8, 7]

controll_button = [16, 20]
player_button = [26, 19, 13, 6, 5]

for i in all_led:
    GPIO.setup(i, GPIO.OUT)

#Programm-Start:
try:
    rolls(all_led, 100)

    #Ende:
    print("Finished")
    GPIO.cleanup()

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
