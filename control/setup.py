import time

from helper import animations

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Setup:
GPIO.setmode(GPIO.BCM)

max_player = 5
active_player = 0

max_life = 1
player_life = []

game_selected = 0

control_led = [14, 15, 18]
player_led = [23, 24, 25, 8, 7]
active_led = []
all_led = [14, 15, 18, 23, 24, 25, 8, 7]

#16 -> Back; 20 -> Next
control_button = [16, 20]
player_button = [26, 19, 13, 6, 5]
active_button = []
all_button = [16, 20, 26, 19, 13, 6, 5]

def initialize():
    for i in all_led:
        GPIO.setup(i, GPIO.OUT)
    for i in all_button:
        GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def subtractLifeFromPlayer(number):
    GPIO.output(active_led[number], 1)

    if player_life[number] == 1:
        GPIO.output(control_led[2], 2)
        time.sleep(1)
        animations.one_blink(control_led[2], 3, 0.5)
    if player_life[number] == 2:
        GPIO.output(control_led[1], 1)
        GPIO.output(control_led[2], 1)
        time.sleep(1)
        animations.one_blink(control_led[1], 3, 0.5)
    if player_life[number] == 3:
        GPIO.output(control_led[0], 1)
        GPIO.output(control_led[1], 1)
        GPIO.output(control_led[2], 1)
        time.sleep(1)
        animations.one_blink(control_led[0], 3, 0.5)
    if player_life[number] >= 4:
        animations.array_on(control_led)
        time.sleep(1)
    time.sleep(1)

    player_life[number] -= 1
    GPIO.output(active_led[number], 0)
    animations.array_off(control_led)

    time.sleep(1)

def areAllPlayerAlive():
    for i in player_life:
        if i <= 0:
            return False
    return True