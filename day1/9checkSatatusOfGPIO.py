import RPi.GPIO as GPIO    # Iimport Raspberry Pi GPIO library
from time import sleep     # Iimport the sleep function from the time module
GPIO.setwarnings(False)    # Iginore warning for now
GPIO.setmode(GPIO.BOARD)     # Uise physical pin numbering

GPIO.setup(3,GPIO.IN)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)

"""
while True:
    if GPIO.input(3):
        print("HIGH")
        GPIO.output(5,GPIO.HIGH)
    else:
      print("LOW")
      GPIO.output(5,GPIO.LOW)
"""
"""

if GPIO.input(3):
    print("high")
    GPIO.output(5,GPIO.HIGH)
else:
    print("low")
    GPIO.output(5,GPIO.LOW)
    
"""


while True:
    if(GPIO.input(3)==1):
        print("high")
        GPIO.output(5,GPIO.HIGH)
    else:
        print("low")
        GPIO.output(5,GPIO.LOW)
