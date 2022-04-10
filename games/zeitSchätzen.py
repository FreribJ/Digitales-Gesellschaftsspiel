import time
import random

from control import setup
from helper import animations, sounds

# GPIO Import
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


# Variablen

#Initialzes Callback
def initialize_callback():
    for switch in setup.active_button:
        GPIO.add_event_detect(switch, GPIO.RISING, callback_zeitspeichern, 200)

# Pseudocode:
# Kurze Erklärung wie das Spiel funktionieren soll: Nach der Spieler- und Lebensauswahl beginnen die Spielrunden. Die LEDs leuchten eine zufällige Anzahl an Sekunden (Wahrscheinlich am besten zwischen 5 und 20 Sekunden oder sowas)
# Nachdem die LEDs wieder aus sind, können die Spieler schätzen wie lange die LEDs wohl geleuchtet haben und ihren Guess in Sekunden durch Knopfdruck hochzählen. 1 Kmopfdruck = 1 Sekunde. Am Ende verlieren Die die am weitesten
# von der Tatsächlichen Zahl entfernt waren ein Leben.
# Ich habe aber wirklich gar keinen Plan mehr von Python

def initializeGame():
#Initialisierung der einzelnen Spieler
GPIO.output(setup.active_led, alle initialisierten Spieler)

#Irgendwas was die LEDs eine Zufällige Zeit lang leuchten lässt
def randomDuration():
   random.randint(5, 20)