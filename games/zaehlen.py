import time
import random

from control import setup
from helper import animations

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

global ran_num

#Zeiten Speichern
def callback_zeitspeichern(switch):
    zeit = time.time()
    global zeiten

    player = setup.active_button.index(switch)
    if zeiten[player] == 0:
        zeiten[player] = zeit

#Initialzes Callback
def initialize_callback():
    for switch in setup.active_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)
