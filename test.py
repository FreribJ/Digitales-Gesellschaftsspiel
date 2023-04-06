import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

zumtesten = []

for i in range(40):
    try:
        print("Trying Pin ", i)
        GPIO.setup(i, GPIO.IN)
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=300)
        zumtesten.append(i)
    except:
        print(i, " ist kein Input")

while True:
    for i in range(len(zumtesten)):
        if GPIO.event_detected(zumtesten[i]):
            print("Es ist: ", i)
    time.sleep(1)
