import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try: 
    t = float(input("период сигнала равен: "))

    while True:
        for i in range(0, 255):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t/256)
        for i in range(255, 0, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t/256)

finally:
     GPIO.output(dac, 0)
     GPIO.cleanup()               