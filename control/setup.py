try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

#Setup:
GPIO.setmode(GPIO.BCM)

max_players = 5

control_led = [14, 15, 18]
player_led = [23, 24, 25, 8, 7]
active_led = []
all_led = [14, 15, 18, 23, 24, 25, 8, 7]
#16 -> Back; 20 -> Next
control_button = [16, 20]
player_button = [26, 19, 13, 6, 5]
active_button = []
all_button = [16, 20, 26, 19, 13, 6, 5]

def initialize():
    for i in all_led:
        GPIO.setup(i, GPIO.OUT)
    for i in all_button:
        GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)