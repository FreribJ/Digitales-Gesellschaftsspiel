#Other Import
import time

#GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Variable Import
import setup

#Variablen
zeit = [0, 0, 0, 0, 0]

def callback_zeitspeichern(spieler):
    print("knopf: ", spieler)
    print(time.time())
    print()

def initialize_callback():
    for i in setup.player_button:
        GPIO.add_event_detect(i, GPIO.RISING, callback_zeitspeichern(i), 200)

def remove_callback():
    for i in setup.player_button:
        GPIO.remove_event_detect(i, GPIO.RISING, callback_zeitspeichern, 200)

def start_reaktionstest():
    initialize_callback()
    while True:
        time.sleep(5)
        print("Warte")