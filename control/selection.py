import time

from control import setup
from control.setup import pi, event_detector
from helper import animations, sounds

import pigpio


def player_selection():
    playeractive = []
    for i in range(setup.max_player):
        playeractive.append(False)

    for i in setup.active_led:
        playeractive[setup.player_led.index(i)] = True
        pi.write(i, 1)

    def player_selected_callback(gpio, level, tick):
        print("callback:", gpio, level, tick)
        prior = playeractive[setup.player_button.index(gpio)]

        playeractive[setup.player_button.index(gpio)] = not prior
        pi.write(setup.player_led[setup.player_button.index(gpio)], not prior)


    # Event-Detect
    for i in setup.all_button:
        pi.callback(i, pigpio.RISING, player_selected_callback)

    abbruch = False
    # event_detector.add_event_detect(setup.control_button[0], 32, bouncetime=300)
    while True:
        time.sleep(1)

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
    pi.write(setup.player_led[setup.max_life - 1], 1)

    # Event-Detect
    for i in setup.all_button:
        if not i == setup.control_button[0]:
            event_detector.add_event_detect(i, 31, bouncetime=300)
        else:
            event_detector.add_event_detect(i, 32, bouncetime=300)

    abbruch = False
    while not event_detector.event_detected(setup.control_button[1]):
        for i in setup.player_button:
            if event_detector.event_detected(i):
                sounds.playButtonPush()
                number = setup.player_button.index(i)
                pi.write(setup.player_led[setup.max_life - 1], 0)
                setup.max_life = number + 1
                pi.write(setup.player_led[setup.max_life - 1], 1)
        if event_detector.event_detected(setup.control_button[0]):
            abbruch = True
            break


    # Remove Event-Detect:
    for i in setup.all_button:
        event_detector.remove_event_detect(i)

    animations.array_off(setup.player_led)

    if abbruch:
        return False

    return True


def game_selection():
    pi.write(setup.player_led[setup.game_selected], 1)

    # Event-Detect
    for i in setup.all_button:
        if not i == setup.control_button[0]:
            event_detector.add_event_detect(i, 31, bouncetime=300)
        else:
            event_detector.add_event_detect(i, 32, bouncetime=300)

    abbruch = False
    while not event_detector.event_detected(setup.control_button[1]):
        for i in setup.player_button:
            if event_detector.event_detected(i):
                sounds.playButtonPush()
                number = setup.player_button.index(i)
                pi.write(setup.player_led[setup.game_selected], 0)
                setup.game_selected = number
                pi.write(setup.player_led[setup.game_selected], 1)
        if event_detector.event_detected(setup.control_button[0]):
            abbruch = True
            break

    # Remove Event-Detect:
    for i in setup.all_button:
        event_detector.remove_event_detect(i)

    animations.array_off(setup.player_led)

    if abbruch:
        return False

    return True
