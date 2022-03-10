try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

controll_led = [14, 15, 18]
player_led = [23, 24, 25, 8, 7]

controll_button = [16, 20]
player_button = [26, 19, 13, 6, 5]

for i in controll_led:
    GPIO.setup(i, GPIO.OUT)

try:
    while True:
        for i in controll_led:
            GPIO.output(i, 1)
            time.sleep(1)
        for i in controll_led:
            GPIO.output(i, 0)
            time.sleep(1)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()