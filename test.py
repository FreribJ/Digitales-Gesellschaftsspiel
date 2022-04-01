import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

led = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.add_event_detect(11, GPIO.BOTH, bouncetime=200)

while True:
    GPIO.output(led, 1)
    if GPIO.event_detected(11):
        print("event detected: ")
    GPIO.output(led, 0)
    if GPIO.event_detected(11):
        print("event detected: ")