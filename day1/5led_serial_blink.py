import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

"""
while True: # Run forever
    GPIO.output(3, GPIO.HIGH) # Turn on
    sleep(0.1) # Sleep for 1 second
    GPIO.output(3, GPIO.LOW) # Turn off
    sleep(0.1) # Sleep for 1 second
    GPIO.output(5, GPIO.HIGH) # Turn off
    sleep(0.1) # Sleep for 1 second
    GPIO.output(5, GPIO.LOW) # Turn off
    sleep(0.1) # Sleep for 1 second
    GPIO.output(13, GPIO.HIGH) # Turn on
    sleep(0.1) # Sleep for 1 second
    GPIO.output(13, GPIO.LOW) # Turn off
    sleep(0.1) # Sleep for 1 second
    GPIO.output(15, GPIO.HIGH) # Turn off
    sleep(0.1) # Sleep for 1 second
    GPIO.output(15, GPIO.LOW) # Turn off
    sleep(0.1) # Sleep for 1 second

"""
i=31
while True:
    for i in range(31,38,2):
        GPIO.output(i, GPIO.HIGH) # Turn off
        sleep(0.1) # Sleep for 1 second
        GPIO.output(i, GPIO.LOW) # Turn off
        sleep(0.1) # Sleep for 1 second
