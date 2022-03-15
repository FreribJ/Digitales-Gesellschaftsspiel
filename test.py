try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)

GPIO.add_event_detect(20, GPIO.RISING, 200)

while True:
    print(GPIO.event_detected(20))