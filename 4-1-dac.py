import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        n = input("введите число от 0 до 255: ")
        
        try:
            n = int(n)
            if 0 <= n <= 255:
                GPIO.output(dac, decimal2binary(n))
                volt = float(n) / 256.0 * 3.3
                print(f"напряжение составляет {volt:.4} вольт")
            else:
                if n < 0 or n > 255 or isinstance(n, float) == 1:
                    print("неподходящее число")
        except Exception:
            if n == "q": break
            
            
                

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
             