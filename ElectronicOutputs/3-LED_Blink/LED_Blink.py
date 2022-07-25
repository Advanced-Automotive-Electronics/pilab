#!/usr/bin/env python
import RPi.GPIO as GPIO
import time # import the library time

PIN_R = 12
counter = 0

GPIO.setmode(GPIO.BOARD)    # Numbers GPIOs by physical location
GPIO.setup(PIN_R, GPIO.OUT) # Set the R pin to mode is output

while counter < 5:
    print ("Start of the program")
    time.sleep(3) # wait for 3 seconds
    print ("Turn on LED")
    GPIO.output(PIN_R, GPIO.HIGH) # Set the R pin to High(3.3V) to turn on led
    time.sleep(3) # wait for 3 seconds
    print ("Turn off LED")
    GPIO.output(PIN_R, GPIO.LOW) # Set the R pin to Low(0V) to turn off led
    counter += 1

print ("End of LED")

GPIO.cleanup() # this ensures a clean exit
