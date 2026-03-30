import time

import pigpio
import threading

from helper import animations, sounds

# Initialize pigpio
pi = pigpio.pi()

# Helper for RPi.GPIO-style event detection
class EventDetector:
    def __init__(self, pi):
        self.pi = pi
        self.events = {}
        self.callbacks = {}

    def add_event_detect(self, gpio, edge, callback=None, bouncetime=200):
        # bouncetime is in ms, pigpio debounce is in microseconds
        # self.pi.set_glitch_filter(gpio, bouncetime)
        
        if edge == 31: # RISING
            pigpio_edge = pigpio.RISING_EDGE
        elif edge == 32: # FALLING
            pigpio_edge = pigpio.FALLING_EDGE
        else: # BOTH
            pigpio_edge = pigpio.EITHER_EDGE
            
        self.events[gpio] = False
        def internal_callback(g, level, tick):
            self.events[g] = True
            if callback:
                callback(g)
            
        self.callbacks[gpio] = self.pi.callback(gpio, pigpio_edge, internal_callback)

    def remove_event_detect(self, gpio):
        if gpio in self.callbacks:
            self.callbacks[gpio].cancel()
            del self.callbacks[gpio]
        if gpio in self.events:
            del self.events[gpio]

    def event_detected(self, gpio):
        if gpio in self.events:
            detected = self.events[gpio]
            self.events[gpio] = False
            return detected
        return False

event_detector = EventDetector(pi)

#Setting:
WAIT_FOR_CONTINUE = True

#Pin-Setup:
device = "pizero"

if device == "raspberrypi3":
    all_led = [15, 13, 11, 29, 21, 8, 12, 18, 24, 32, 38, 37, 33]
    all_button = [23, 31, 5, 35, 16, 10, 22, 26, 36, 40, 19, 7]
elif device == "pizero":
    all_led = [22, 27, 17, 5, 9, 14, 18, 24, 8, 12, 20, 26, 13]
    all_button = [3, 4, 11, 10, 15, 23, 25, 7, 16, 21, 19, 6]


#First -> Back; Second -> Next
control_button = [all_button[0], all_button[1]]
control_led = [all_led[0], all_led[1], all_led[2]]
player_led = [all_led[3], all_led[4], all_led[5], all_led[6], all_led[7], all_led[8], all_led[9], all_led[10], all_led[11], all_led[12]]
player_button = [all_button[2], all_button[3], all_button[4], all_button[5], all_button[6], all_button[7], all_button[8], all_button[9], all_button[10], all_button[11]]
max_player = len(player_button)

active_player = 0
active_button = []
active_led = []

max_life = 1
player_life = []

game_selected = 0

def initialize():
    # sounds.initialize()

    for i in all_led:
        pi.set_mode(i, pigpio.OUTPUT)
    for i in all_button:
        pi.set_mode(i, pigpio.INPUT)
        pi.set_pull_up_down(i, pigpio.PUD_OFF)

#Removes Callback
def remove_eventDetect():
    for i in active_button:
        event_detector.remove_event_detect(i)

def reset_eventDetect():
    for i in active_button:
        event_detector.event_detected(i)

def add_eventDetect(bouncetime_ms):
    for i in active_button:
        event_detector.add_event_detect(i, 31, bouncetime=bouncetime_ms) # 31 = GPIO.RISING

def subtractLifeFromPlayer(loser_num):

    animations.all_blink(5, 0.3)

    substractLifeAnimation(loser_num)

    player_life[loser_num] -= 1
    animations.array_off(control_led)

    time.sleep(1)

def subtractLifeFromPlayerArray(loser_num):

    animations.all_blink(5, 0.3)

    for i in loser_num:
        substractLifeAnimation(i)
        player_life[i] -= 1

    animations.array_off(control_led)
    time.sleep(1)

def subtractLifeFromPlayerArrayWithWinner(loser_num, winner_num):

    animations.all_blink(5, 0.3)

    animations.one_blink(active_led[winner_num], 5, 0.2)
    for i in loser_num:
        substractLifeAnimation(i)
        player_life[i] -= 1

    animations.array_off(control_led)
    time.sleep(1)

def subtractLifeFromPlayerArrayWithWinnerArray(loser_num, winner_num):

    animations.all_blink(5, 0.3)
    time.sleep(1)

    winner_led = []
    for i in winner_num:
        winner_led.append(active_led[i])
    animations.array_blink(winner_led, 5, 0.2)
    for i in loser_num:
        substractLifeAnimation(i)
        player_life[i] -= 1

    animations.array_off(control_led)
    time.sleep(1)

#!!!Duplicate as method above!!!
def subtractLifeFromPlayerWithWinner(loser_num, winner_num):
    animations.all_blink(5, 0.3)

    animations.one_blink(active_led[winner_num], 5, 0.2)

    substractLifeAnimation(loser_num)

    player_life[loser_num] -= 1
    animations.array_off(control_led)

    time.sleep(1)

def substractLifeAnimation(loser_num):
    sounds.playLoseSound()
    pi.write(active_led[loser_num], 1)

    if player_life[loser_num] == 1:
        pi.write(control_led[2], 1) # Note: the original code had 2 here, which might have been a typo for 1 in GPIO.output
        time.sleep(1)
        animations.one_blink(control_led[2], 3, 0.5)
    if player_life[loser_num] == 2:
        pi.write(control_led[1], 1)
        pi.write(control_led[2], 1)
        time.sleep(1)
        animations.one_blink(control_led[1], 3, 0.5)
    if player_life[loser_num] == 3:
        pi.write(control_led[0], 1)
        pi.write(control_led[1], 1)
        pi.write(control_led[2], 1)
        time.sleep(1)
        animations.one_blink(control_led[0], 3, 0.5)
    if player_life[loser_num] >= 4:
        animations.array_on(control_led)
        time.sleep(1)

    time.sleep(1)
    pi.write(active_led[loser_num], 0)

def waitForContinue():
    if WAIT_FOR_CONTINUE:
        event_detector.add_event_detect(control_button[0], 32, bouncetime=200) # 32 = GPIO.FALLING
        event_detector.add_event_detect(control_button[1], 31, bouncetime=200) # 31 = GPIO.RISING

        while not event_detector.event_detected(control_button[1]):
            time.sleep(0.5)
            pi.write(control_led[1], 1)
            time.sleep(0.5)
            pi.write(control_led[1], 0)
            if event_detector.event_detected(control_button[0]):
                for i in range(len(player_life)):
                    player_life[i] = 0
                break

        event_detector.remove_event_detect(control_button[0])
        event_detector.remove_event_detect(control_button[1])


def areAllPlayerAlive():
    for i in player_life:
        if i <= 0:
            return False
    return True