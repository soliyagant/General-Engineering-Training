import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24, 0.5)
p.start(0)


try:
    while True:
        dc = int(input())
        p.ChangeDutyCycle(dc)
        print("{:.2f}".format(dc*3.3/100))
finally:
    p.stop()
    GPIO.output(24, 0)
    GPIO.cleanup()
p.stop()
GPIO.cleanup()