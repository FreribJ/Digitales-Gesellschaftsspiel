import time

from helper import animations

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Setting:
WAIT_FOR_CONTINUE = True

###For Raspberry Pi 3:
#all_led = [22, 27, 17, 5, 9, 14, 18, 24, 8, 12, 20, 26, 13]
#all_button = [3, 4, 11, 10, 15, 23, 25, 7, 16, 21, 19, 6]

##For Banana Pi M2 Zero:
all_button = [5, 7, 23, 19, 10, 16, 22, 26, 36, 40, 35, 31]
all_led = [15, 13, 11, 29, 21, 8, 12, 18, 24, 32, 38, 37, 33]

#3 -> Back; 4 -> Next
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

    GPIO.setmode(GPIO.BOARD)
    for i in all_led:
        GPIO.setup(i, GPIO.OUT)
    for i in all_button:
        GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

#Removes Callback
def remove_eventDetect():
    for i in active_button:
        GPIO.remove_event_detect(i)

def reset_eventDetect():
    for i in active_button:
        GPIO.event_detected(i)

def add_eventDetect(bouncetime_ms):
    for i in active_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=bouncetime_ms)

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
    GPIO.output(active_led[loser_num], 1)

    if player_life[loser_num] == 1:
        GPIO.output(control_led[2], 2)
        time.sleep(1)
        animations.one_blink(control_led[2], 3, 0.5)
    if player_life[loser_num] == 2:
        GPIO.output(control_led[1], 1)
        GPIO.output(control_led[2], 1)
        time.sleep(1)
        animations.one_blink(control_led[1], 3, 0.5)
    if player_life[loser_num] == 3:
        GPIO.output(control_led[0], 1)
        GPIO.output(control_led[1], 1)
        GPIO.output(control_led[2], 1)
        time.sleep(1)
        animations.one_blink(control_led[0], 3, 0.5)
    if player_life[loser_num] >= 4:
        animations.array_on(control_led)
        time.sleep(1)

    time.sleep(1)
    GPIO.output(active_led[loser_num], 0)

def waitForContinue():
    if WAIT_FOR_CONTINUE:
        GPIO.add_event_detect(control_button[0], GPIO.FALLING, bouncetime=200)
        GPIO.add_event_detect(control_button[1], GPIO.RISING, bouncetime=200)

        while not GPIO.event_detected(control_button[1]):
            time.sleep(0.5)
            GPIO.output(control_led[1], 1)
            time.sleep(0.5)
            GPIO.output(control_led[1], 0)
            if GPIO.event_detected(control_button[0]):
                for i in range(len(player_life)):
                    player_life[i] = 0
                break

        GPIO.remove_event_detect(control_button[0])
        GPIO.remove_event_detect(control_button[1])


def areAllPlayerAlive():
    for i in player_life:
        if i <= 0:
            return False
    return True