import RPi.GPIO as GPIO    # Iimport Raspberry Pi GPIO library
from time import sleep     # Iimport the sleep function from the time module
GPIO.setwarnings(False)    # Iginore warning for now
GPIO.setmode(GPIO.BCM)   # Uise physical pin numbering
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

while True: # Run forever
    #GPIO.output(8, GPIO.HIGH) # Turn on
    GPIO.output(6, GPIO.HIGH) # Turn on
    GPIO.output(13, GPIO.HIGH) # Turn on
    GPIO.output(19, GPIO.HIGH) # Turn on
    GPIO.output(26, GPIO.HIGH) # Turn on
