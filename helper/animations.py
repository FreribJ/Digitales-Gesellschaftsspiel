try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO
import time
from control import setup


def rolls(leds, times):
    for t in range(times):
        for i in leds:
            GPIO.output(i, 1)
            time.sleep(0.05)
        for i in leds:
            GPIO.output(i, 0)
            time.sleep(0.05)

def all_blink(times, time_sleep):
    for t in range(times):
        for i in setup.player_led:
            GPIO.output(i, 1)
        time.sleep(time_sleep)
        for i in setup.all_led:
            GPIO.output(i, 0)
        if not t == times-1:
            time.sleep(time_sleep)

def all_off():
    for i in setup.all_led:
        GPIO.output(i, 0)

def all_on():
    for i in setup.all_led:
        GPIO.output(i, 1)


def array_off(leds):
    for i in leds:
        GPIO.output(i, 0)


def array_on(leds):
    for i in leds:
        GPIO.output(i, 1)

def one_blink(led, times, time_sleep):
    for t in range(times):
        GPIO.output(led, 1)
        time.sleep(time_sleep)
        GPIO.output(led, 0)
        if not t == times-1:
            time.sleep(time_sleep)