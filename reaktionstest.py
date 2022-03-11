#Other Import
import time

#GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Variable Import
from main import player_button

#Variablen
zeit = [0, 0, 0, 0, 0]

def callback_zeitspeichern(spieler):
    print("knopf: " + spieler)
    print(time.time())
    print()

def initialize_callback():
    for i in player_button:
        GPIO.add_event_detect(i, GPIO.RISING, callback_zeitspeichern(i), 200)

def start_reaktionstest():
    time.sleep(5)
    print("Warte")