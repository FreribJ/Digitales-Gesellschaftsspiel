import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)

GPIO.add_event_detect(11, GPIO.RISING)

while True:
    if GPIO.event_detected(11):
        print("event detected: ")