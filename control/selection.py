from control import setup
from helper import animations

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


def playerselection():
    playeractive = [False, False, False, False, False]
    for i in setup.active_led:
        playeractive[setup.all_led.index(i)] = True
        GPIO.output(i, 1)

    for i in setup.player_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=2000)

    while True:
        for i in setup.player_button:
            if GPIO.event_detected(i):
                number = setup.player_button.index(i)
                if playeractive[number]:
                    playeractive[number] = False
                    GPIO.output(setup.player_led[number], 0)
                else:
                    playeractive[number] = True
                    GPIO.output(setup.player_led[number], 1)

    animations.all_off()

