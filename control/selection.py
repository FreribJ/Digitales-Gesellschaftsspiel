import time

from control import setup
from helper import animations, sounds

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


def player_selection():
    playeractive = []
    for i in range(setup.max_player):
        playeractive.append(False)

    for i in setup.active_led:
        playeractive[setup.player_led.index(i)] = True
        GPIO.output(i, 1)

    # Event-Detect
    for i in setup.all_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=1000)

    sounds.test1()

    abbruch = False
    while not (GPIO.event_detected(setup.control_button[1]) and not sum(playeractive) <= 1): #Wartet auf Next, beachtet aber, dass mindestens ein Spieler ausgewählt wurde
        for i in setup.player_button:
            if GPIO.event_detected(i):
                sounds.test2()
                number = setup.player_button.index(i)
                if playeractive[number]:
                    playeractive[number] = False
                    GPIO.output(setup.player_led[number], 0)
                else:
                    playeractive[number] = True
                    GPIO.output(setup.player_led[number], 1)
        if GPIO.event_detected(setup.control_button[0]):
            abbruch = True
            break

    # Remove Event-Detect:
    for i in setup.all_button:
        GPIO.remove_event_detect(i)

    # Einstellungen speichern
    setup.active_player = 0
    setup.active_button = []
    setup.active_led = []

    for i in range(setup.max_player):
        if playeractive[i]:
            setup.active_button.append(setup.player_button[i])
            setup.active_led.append(setup.player_led[i])
            setup.active_player += 1

    animations.array_off(setup.player_led)

    if abbruch:
        return False

    return True


def life_selection():
    GPIO.output(setup.player_led[setup.max_life - 1], 1)

    # Event-Detect
    for i in setup.all_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=1000)

    abbruch = False
    while not GPIO.event_detected(setup.control_button[1]):
        for i in setup.player_button:
            if GPIO.event_detected(i):
                sounds.playButtonPush()
                number = setup.player_button.index(i)
                GPIO.output(setup.player_led[setup.max_life - 1], 0)
                setup.max_life = number + 1
                GPIO.output(setup.player_led[setup.max_life - 1], 1)
        if GPIO.event_detected(setup.control_button[0]):
            abbruch = True
            break


    # Remove Event-Detect:
    for i in setup.all_button:
        GPIO.remove_event_detect(i)

    animations.array_off(setup.player_led)

    if abbruch:
        return False

    return True


def game_selection():
    GPIO.output(setup.player_led[setup.game_selected], 1)

    # Event-Detect
    for i in setup.all_button:
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=1000)


    abbruch = False
    while not GPIO.event_detected(setup.control_button[1]):
        for i in setup.player_button:
            if GPIO.event_detected(i):
                sounds.playButtonPush()
                number = setup.player_button.index(i)
                GPIO.output(setup.player_led[setup.game_selected], 0)
                setup.game_selected = number
                GPIO.output(setup.player_led[setup.game_selected], 1)
        if GPIO.event_detected(setup.control_button[0]):
            abbruch = True
            break

    # Remove Event-Detect:
    for i in setup.all_button:
        GPIO.remove_event_detect(i)

    animations.array_off(setup.player_led)

    if abbruch:
        return False

    return True
