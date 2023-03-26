import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setup(leds, GPIO.OUT)
for i in range(3):
    for j in leds:
        GPIO.output(j, 1)
        time.sleep(0.2)
GPIO.output(leds, 0)
GPIO.cleanup()
