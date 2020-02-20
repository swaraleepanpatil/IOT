#Hardware connection
#DHT11 VCC to 5v Rpi
#DHT11 GND to Gnd Rpi
#DHT11 data to 
import sys
import Adafruit_DHT

import RPi.GPIO as GPIO    # Iimport Raspberry Pi GPIO library
from time import sleep     # Iimport the sleep function from the time module
GPIO.setwarnings(False)    # Iginore warning for now
GPIO.setmode(GPIO.BCM)   # Uise physical pin numbering
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
while True: # Run forever
    humidity, temperature = Adafruit_DHT.read_retry(11, 18)#GPIO 18 by BCM std
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    if temperature>=32:
        GPIO.output(2, GPIO.HIGH) # Turn on
        print("Its ",temperature)
    else:
        GPIO.output(2, GPIO.LOW) # Turn off
"""
output:-
Temp: 31.0 C  Humidity: 58.0 %
Temp: 31.0 C  Humidity: 60.0 %
Temp: 31.0 C  Humidity: 62.0 %
Temp: 31.0 C  Humidity: 95.0 %
Temp: 31.0 C  Humidity: 95.0 %
Temp: 31.0 C  Humidity: 91.0 %
Temp: 31.0 C  Humidity: 87.0 %
Temp: 31.0 C  Humidity: 74.0 %
Temp: 31.0 C  Humidity: 71.0 %
Temp: 31.0 C  Humidity: 70.0 %
Temp: 31.0 C  Humidity: 69.0 %
Temp: 31.0 C  Humidity: 69.0 %
Temp: 31.0 C  Humidity: 62.0 %
Temp: 31.0 C  Humidity: 66.0 %
Temp: 31.0 C  Humidity: 54.0 %
Temp: 31.0 C  Humidity: 43.0 %
Temp: 31.0 C  Humidity: 40.0 %
Temp: 31.0 C  Humidity: 44.0 %
Temp: 31.0 C  Humidity: 53.0 %
Temp: 31.0 C  Humidity: 59.0 %
Temp: 31.0 C  Humidity: 61.0 %
Temp: 32.0 C  Humidity: 63.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 51.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 39.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 36.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 34.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 32.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 31.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 30.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 29.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 29.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 28.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 28.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 27.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 27.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 27.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 27.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 27.0 %
('Its ', 32.0)
Temp: 32.0 C  Humidity: 27.0 %
('Its ', 32.0)
Temp: 31.0 C  Humidity: 29.0 %
Temp: 31.0 C  Humidity: 29.0 %
Temp: 31.0 C  Humidity: 28.0 %
"""
