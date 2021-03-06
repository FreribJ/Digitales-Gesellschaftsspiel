import time

from games import hotPotato, reaktionstest, pingPong, fourColorGame, zaehlen, auslassen, jerusalem, zeitSchätzen
from helper import animations, sounds
from control import setup, selection

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Programm-Initialize:
setup.initialize()

#Programm-Start:
try:
    #Startanimation:
    print("Started")
    animations.rolls(setup.all_led, 1)

    menu_level = 0
    exit_check = 0
    while True:
        #Spielerauswahl:
        if menu_level == 0:
            print("Spielerauswahl")
            GPIO.output(setup.control_led[0], 1)
            next_menu = selection.player_selection()
            sounds.playMenuSound()
            animations.rolls(setup.player_led, 1)
            GPIO.output(setup.control_led[0], 0)
            if next_menu:
                menu_level = 1
                exit_check = 0
            else:
                #Auf Standard Resetten:
                setup.active_led = []
                setup.active_button = []
                setup.game_selected = 0
                setup.max_life = 1
                exit_check += 1
                if exit_check >= 3:
                    break

        #Lebenwahl:
        if menu_level == 1:
            print("Lebenauswahl")
            GPIO.output(setup.control_led[1], 1)
            next_menu = selection.life_selection()
            sounds.playMenuSound()
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
            sounds.playMenuSound()
            animations.rolls(setup.player_led, 1)
            GPIO.output(setup.control_led[2], 0)
            if next_menu:
                menu_level = 3
            else:
                menu_level = 1

        #Spielstart:
        if menu_level == 3:
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
                print("Game -> Simon Says")
                fourColorGame.startGame()

            elif setup.game_selected == 3:
                print("Game -> Zählen")
                zaehlen.startGame()

            elif setup.game_selected == 4:
                print("Game -> PingPong")
                pingPong.startGame()

            elif setup.game_selected == 5:
                print("Game -> Zeit schätzen")
                zeitSchätzen.startGame()

            elif setup.game_selected == 6:
                print("Game -> Auslassen")
                auslassen.startGame()

            elif setup.game_selected == 7:
                print("Game -> Jerusalem")
                jerusalem.startGame()

            elif setup.game_selected == 8:
                print("Game -> Empty")

            elif setup.game_selected == 9:
                print("Game -> Empty")

            #Ende
            animations.rolls(setup.player_led, 1)
            menu_level = 2

    #Ende:
    animations.rolls(setup.all_led, 1)
    GPIO.cleanup()
    time.sleep(1)
    print("Finished")

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
