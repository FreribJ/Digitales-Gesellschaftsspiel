try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

all_button = [3, 4, 15, 23, 25, 7, 16, 21, 19, 6, 11, 10]

for i in all_button:
    print(i, " -> ", all_button.index(i))
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)