import RPi.GPIO as GPIO
import time

def dec2bin(N):
return[int(i) for i in bin(N)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        T = float(input()) # период
        N = 0
    while N < 256:
        GPIO.output(dac, dec2bin(int(N)))
        print("{:.4f}".format(N * 3.3 / 256))
        time.sleep(T/(256*2))
        N += 1
        N = 255
    while N >= 0:
        GPIO.output(dac, dec2bin(int(int(N))))
        print("{:.4f}".format(N * 3.3 / 256))
        time.sleep(T/(256*2))
        N -= 1
        GPIO.output(dac, 0)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
GPIO.output(dac, 0)
GPIO.cleanup()