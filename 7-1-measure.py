import RPi.GPIO as GPIO
import matplotlib.pyplot as plot
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    temp = 0
    for rank in range(7, -1, -1):
        temp += 2**rank
        GPIO.output(dac, decimal2binary(temp))
        time.sleep(0.01)
        cmpv = GPIO.input(cmp)
        if (cmpv == 1):
            temp -= 2**rank

    return temp

def translate_leds(value):
    temp = decimal2binary(value)
    GPIO.output(leds, temp)
    return 0

def current_time():
    return time.time()-time0


dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
cmp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(cmp, GPIO.IN)



time_res = []
data_res = []

try:
    GPIO.output(troyka, 1)
    time0 = time.time()

    value = 0
    while (value < 200):
        value = adc()
        #translate_leds(value)
        print(value)
        time_res.append(current_time())
        data_res.append(value)
    
    GPIO.output(troyka, 0)

    while (value > 10):
        value = adc()
        print(value)
        translate_leds(value)

        time_res.append(current_time())
        data_res.append(value)

    time1 = time.time()

    #saving
    plot.plot(time_res, data_res)
    plot.show()

    with open("./plot.txt", 'w') as f:
        f.write(str((time1 - time0) / len(data_res)))
        f.write("\n")
        
        time_str = [str(item) for item in time_res]
        data_str = [str(item) for item in data_res]
        f.write("\n".join(data_str))

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()


