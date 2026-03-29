from control.setup import pi
import time
from control import setup


def rolls(leds, times):
    for t in range(times):
        for i in leds:
            pi.write(i, 1)
            time.sleep(0.05)
        for i in leds:
            pi.write(i, 0)
            time.sleep(0.05)

def rings(leds, times, time_sleep):
    arr_len = len(leds)
    time_sleep = time_sleep / 2
    for i in range(times):
        led = leds[i % arr_len]
        time.sleep(time_sleep)
        pi.write(led, 1)
        time.sleep(time_sleep)
        pi.write(led, 0)

def all_blink(times, time_sleep):
    for t in range(times):
        for i in setup.player_led:
            pi.write(i, 1)
        time.sleep(time_sleep)
        for i in setup.all_led:
            pi.write(i, 0)
        if not t == times-1:
            time.sleep(time_sleep)

def all_off():
    for i in setup.all_led:
        pi.write(i, 0)

def all_on():
    for i in setup.all_led:
        pi.write(i, 1)


def array_off(leds):
    for i in leds:
        pi.write(i, 0)


def array_on(leds):
    for i in leds:
        pi.write(i, 1)

def one_blink(led, times, time_sleep):
    for t in range(times):
        pi.write(led, 1)
        time.sleep(time_sleep)
        pi.write(led, 0)
        if not t == times-1:
            time.sleep(time_sleep)

def array_blink(leds, times, time_sleep):
    for t in range(times):
        for i in leds:
            pi.write(i, 1)
        time.sleep(time_sleep)
        for i in leds:
            pi.write(i, 0)
        if not t == times-1:
            time.sleep(time_sleep)
