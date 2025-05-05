import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 1000)
p.start(0)

try:
    while True:
        f = int(input())
        p.ChangeDutyCycle(f)
        print((3.3*f) /100)

finally:
    p.stop()
    GPIO.output(17,0)
    GPIO.cleanup()