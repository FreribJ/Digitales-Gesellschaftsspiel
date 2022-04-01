import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)
GPIO.setup(5, GPIO.OUT)

GPIO.add_event_detect(11, GPIO.BOTH, bouncetime=200)

while True:
    GPIO.output(5, 1)
    if GPIO.event_detected(11):
        print("event detected: ")
    GPIO.output(5, 0)
    if GPIO.event_detected(11):
        print("event detected: ")