# blink LED lights

import time
import random
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

#define your output GPIOs
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

#while loop to open and close the lights untill you stop the operation
while True:
    x= random.randint(11,15)
    y= random.randint(11,15)
    if (x != y and x!=14 and y!=14):
        GPIO.output(x, GPIO.HIGH)
        GPIO.output(y, GPIO.HIGH)
        time.sleep(0.15)
        GPIO.output(x, GPIO.LOW)
        GPIO.output(y, GPIO.LOW)

