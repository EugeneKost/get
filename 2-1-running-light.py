import RPi.GPIO as GPIO
import time as time
GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
count = 0


GPIO.setup(leds,GPIO.OUT)

for i in range (3):
    for i in leds:
        GPIO.output(int(i),1)
        time.sleep(0.2)
        GPIO.output(int(i),0)

GPIO.cleanup()
