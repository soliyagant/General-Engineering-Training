import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setup(dac, GPIO.OUT)

number_random = [0, 0, 0, 1, 1, 1, 1, 1]
GPIO.output(dac, number_random) # with random 2-bit number
time.sleep(10)

number2 = [0, 0, 0, 0, 0, 0, 1, 0]
GPIO.output(dac, number2) # with 2
time.sleep(10)

number5 = [0, 0, 0, 0, 0, 1, 0, 1]
GPIO.output(dac, number2) # with 5, for example
time.sleep(10)

# the same script goes for 32, 64, 127, 255. 256 can't be presented using 8 led lights.
GPIO.output(dac, 0)
GPIO.cleanup()
