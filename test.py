import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

for i in range(40):
    try:
        print("Trying Pin ", i)
        GPIO.setup(i, GPIO.IN)
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=300)
        time.sleep(4)
    except:
        print(i, " ist kein Output")

while True:
    for i in range(40):
        if GPIO.event_detected(i):
            print("Es ist: ", i)
    time.sleep(1)
