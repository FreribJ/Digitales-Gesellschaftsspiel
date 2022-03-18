import time

from games import hotPotato, reaktionstest, pingPong
from helper import animations
from control import setup, selection
from tests import test1, test2

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Sets all lives to 1 for a last round
def callbackEndGame(switch):
    for i in range(len(setup.player_life)):
        setup.player_life[i] = 1

#Programm-Initialize:
setup.initialize()

#Programm-Start:
try:
    #Startanimation:
    print("Started")
    animations.rolls(setup.all_led, 1)

    menu_level = 0
    while True:
        #Spielerauswahl:
        if menu_level == 0:
            print("Spielerauswahl")
            GPIO.output(setup.control_led[0], 1)
            next_menu = selection.player_selection()
            animations.rolls(setup.player_led, 1)
            GPIO.output(setup.control_led[0], 0)
            if next_menu:
                menu_level = 1
            else:
                break

        #Lebenwahl:
        if menu_level == 1:
            print("Lebenauswahl")
            GPIO.output(setup.control_led[1], 1)
            next_menu = selection.life_selection()
            animations.rolls(setup.player_led, 1)
            GPIO.output(setup.control_led[1], 0)
            if next_menu:
                menu_level = 2
            else:
                menu_level = 0

        #Spielauswahl:
        if menu_level == 2:
            print("Spielauswahl")
            GPIO.output(setup.control_led[2], 1)
            next_menu = selection.game_selection()
            animations.rolls(setup.player_led, 1)
            GPIO.output(setup.control_led[2], 0)
            if next_menu:
                menu_level = 3
            else:
                menu_level = 1

        #Spielstart:
        if menu_level == 3:
            #Abbruch einstellen
            GPIO.add_event_detect(setup.control_button[0], GPIO.RISING, callbackEndGame, 200)

            #Leben Resetten
            setup.player_life = []
            for i in range(setup.active_player):
                setup.player_life.append(setup.max_life)

            #Spielaufruf
            time.sleep(1)
            if setup.game_selected == 0:
                print("Game -> Reaktionstest")
                reaktionstest.startGame()
            elif setup.game_selected == 1:
                print("Game -> Hot Potato")
                hotPotato.startGame()
            elif setup.game_selected == 2:
                print("Game -> test1")
                test1.startGame()
            elif setup.game_selected == 3:
                print("Game -> test2")
                test2.startGame()
            elif setup.game_selected == 4:
                print("Game -> PingPong")
                pingPong.startGame()

            #Ende
            GPIO.remove_event_detect(setup.control_button[0])
            animations.rolls(setup.player_led, 1)
            menu_level = 2

    #Ende:
    animations.rolls(setup.all_led, 1)
    print("Finished")
    GPIO.cleanup()

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
