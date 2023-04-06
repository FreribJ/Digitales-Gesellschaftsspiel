import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

zumtesten = []

for i in range(40):
    try:
        GPIO.setup(i, GPIO.IN)
        GPIO.add_event_detect(i, GPIO.RISING, bouncetime=300)
        zumtesten.append(i)
        print("OUTPUT PIN: ", i)
    except:
        print()

print(zumtesten)

while True:
    for i in range(len(zumtesten)):
        if GPIO.event_detected(zumtesten[i]):
            print("Es ist: ", zumtesten[i])
            time.sleep(0.01)
    time.sleep(1)
