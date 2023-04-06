import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

zumtesten = []

for i in range(40):
    try:
        GPIO.setup(i+1, GPIO.IN)
        GPIO.add_event_detect(i+1, GPIO.RISING, bouncetime=300)
        zumtesten.append(i+1)
        print("OUTPUT PIN: ", i+1)
    except:
        print()

print(zumtesten)

while True:
    for i in range(len(zumtesten)):
        if GPIO.event_detected(zumtesten[i]):
            print("Es ist: ", zumtesten[i])
        if GPIO.input(zumtesten[i]):
            print("Input: ", zumtesten[i])
        time.sleep(0.1)
    time.sleep(1)
    print("Test")
