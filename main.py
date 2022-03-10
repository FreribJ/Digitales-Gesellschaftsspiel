try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

controll_led = [14, 15, 18]

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