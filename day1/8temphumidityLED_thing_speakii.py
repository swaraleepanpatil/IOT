import RPi.GPIO as GPIO    # Iimport Raspberry Pi GPIO library
from time import sleep     # Iimport the sleep function from the time module
GPIO.setwarnings(False)    # Iginore warning for now
GPIO.setmode(GPIO.BCM)     # Uise physical pin numbering

GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)

import sys
import urllib2 #to link data to server
from time import sleep
import Adafruit_DHT 
# Enter Your API key here
myAPI = 'MEI9RH21D5CACGH9'#Key form thing speak 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

while True:
        humi, temp = Adafruit_DHT.read_retry(11, 2)

        if temp>=32:
            GPIO.output(19, GPIO.HIGH) # Turn on
            print("LED : GLOW ",temp)
        else:
            GPIO.output(19, GPIO.LOW) # Turn off
            
        print 'Temp: {0:0.2f} C  Humidity: {1:0.2f} %'.format(temp, humi)
        humi = '%.2f' % humi 					   
        temp = '%.2f' % temp
        
        # Sending the data to thingspeak
        conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (temp, humi))
        print conn.read()
                # Closing the connection

        conn.close()
        # DHT22 requires 2 seconds to give a reading, so make sure to add delay of above 2 seconds.
        sleep(20)
"""
output:-
Temp: 30.00 C  Humidity: 28.00 %
57
Temp: 30.00 C  Humidity: 29.00 %
58
Temp: 30.00 C  Humidity: 28.00 %
59
Temp: 31.00 C  Humidity: 29.00 %
60
Temp: 31.00 C  Humidity: 33.00 %
61
Temp: 31.00 C  Humidity: 33.00 %
62
Temp: 31.00 C  Humidity: 45.00 %
63
Temp: 31.00 C  Humidity: 35.00 %
64
Temp: 31.00 C  Humidity: 29.00 %
65
('LED : GLOW ', 32.0)
Temp: 32.00 C  Humidity: 28.00 %
66
('LED : GLOW ', 32.0)
Temp: 32.00 C  Humidity: 52.00 %
67
Temp: 31.00 C  Humidity: 30.00 %
68

"""
