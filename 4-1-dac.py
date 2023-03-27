import RPi.GPIO as GPIO
import sys

def decimal2binary(N):
return[int(i) for i in bin(int(N))[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)


try:
    while True:
        N = input()
    if N == 'q':
        sys.exit()
    elif not N.isdigit() and ("-" not in N):
        print("N is not a number")
    elif int(N) < 0:
        print("N is below zero")
    elif not N.isdigit() and int(N) % 1 != 0:
        print("N is not integer")
    elif int(N) > 255:
        print("N is out of range")
    else:
        GPIO.output(dac, decimal2binary(N))
        print("{:.4f}".format(3.3*int(N)/256))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
GPIO.output(dac, 0)
GPIO.cleanup()