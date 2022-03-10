try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO
import time
from animations import *

GPIO.setmode(GPIO.BCM)

controll_led = [14, 15, 18]
player_led = [23, 24, 25, 8, 7]
all_led = player_led.append(controll_led)

controll_button = [16, 20]
player_button = [26, 19, 13, 6, 5]

for i in controll_led:
    GPIO.setup(i, GPIO.OUT)

try:
    rolls(all_led, 5)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()