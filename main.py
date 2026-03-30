# import time

# from games import hotPotato, reaktionstest, pingPong, fourColorGame, zaehlen, auslassen, jerusalem, zeitSchätzen
from helper import animations, sounds
from control import setup, selection

from control.setup import pi

#Programm-Initialize:
setup.initialize()

#Programm-Start:

#Startanimation:
print("Started")
animations.rolls(setup.all_led, 1)

menu_level = 0
exit_check = 0

print("Spielerauswahl")
pi.write(setup.control_led[0], 1)
next_menu = selection.player_selection()
sounds.playMenuSound()
animations.rolls(setup.player_led, 1)
pi.write(setup.control_led[0], 0)
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
        print("exit")

