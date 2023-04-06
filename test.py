try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

for i in range(40):
    try:
        print("Trying Pin ", i)
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
    except:
        print(i, " ist kein Output")