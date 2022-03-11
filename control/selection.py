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

    #Event-Detect
    for i in setup.all_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=1000)

    while not (GPIO.event_detected(setup.control_button[0]) or GPIO.event_detected(setup.control_button[1])):
        for i in setup.player_button:
            if GPIO.event_detected(i):
                number = setup.player_button.index(i)
                if playeractive[number]:
                    playeractive[number] = False
                    GPIO.output(setup.player_led[number], 0)
                else:
                    playeractive[number] = True
                    GPIO.output(setup.player_led[number], 1)

    #Remove Event-Detect:
    for i in setup.all_button:
        GPIO.remove_event_detect(i)

    for i in range(5):
        if playeractive[i]:
            setup.active_button.append(setup.player_button[i])
            setup.active_led.append(setup.player_led[i])

    print(setup.active_led)
    print(setup.active_button)

    animations.all_off()

