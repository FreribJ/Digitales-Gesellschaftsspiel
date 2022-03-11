try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO
import time
import setup

def rolls(leds, times):
    for t in range(times):
        for i in leds:
            GPIO.output(i, 1)
            time.sleep(0.1)
        for i in leds:
            GPIO.output(i, 0)
            time.sleep(0.1)

def blink(time_sleep):
    for i in setup.all_led:
        GPIO.output(i, 1)
    time.sleep(time_sleep)
    for i in setup.all_led:
        GPIO.output(i, 0)
