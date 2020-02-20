import RPi.GPIO as GPIO    # Iimport Raspberry Pi GPIO library
from time import sleep     # Iimport the sleep function from the time module
GPIO.setwarnings(False)    # Iginore warning for now
GPIO.setmode(GPIO.BOARD)   # Uise physical pin numbering
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

while True: # Run forever
    #GPIO.output(8, GPIO.HIGH) # Turn on
    GPIO.output(3, GPIO.HIGH) # Turn on
    GPIO.output(5, GPIO.HIGH) # Turn on
    GPIO.output(7, GPIO.HIGH) # Turn on
    GPIO.output(15, GPIO.HIGH) # Turn on
