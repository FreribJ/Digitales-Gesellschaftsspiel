from control import setup
from helper import animations

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


def playerselection():

    playeractive = []
    for i in range(setup.max_player):
        playeractive.append(False)

    for i in setup.active_led:
        playeractive[setup.all_led.index(i)] = True
        GPIO.output(i, 1)

    #Event-Detect
    for i in setup.player_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=1000)
    GPIO.add_event_detect(setup.control_button[1], GPIO.RISING, bouncetime=1000)

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

    #Einstellungen speichern
    setup.active_player = 0
    setup.active_button = []
    setup.active_led = []

    for i in range(setup.max_player):
        if playeractive[i]:
            setup.active_button.append(setup.player_button[i])
            setup.active_led.append(setup.player_led[i])
            setup.active_player += 1

    animations.all_off()

