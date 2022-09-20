import RPi.GPIO as GPIO
import time as time
GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
aux_input = []
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(aux,GPIO.IN)

while True:
    for i in range(8):
        print(i)
        GPIO.output(leds[i],GPIO.input(aux[i]))
    
