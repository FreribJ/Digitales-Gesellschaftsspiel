from control import setup

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


def playerselection():
    player = []

    for i in setup.player_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=200)
    while True:
        for i in setup.player_button:
            if GPIO.event_detected(i):
                print(i)
