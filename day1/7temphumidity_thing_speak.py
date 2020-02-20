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
Temp: 29.00 C  Humidity: 34.00 %
4
Temp: 29.00 C  Humidity: 29.00 %
5
Temp: 30.00 C  Humidity: 29.00 %
6
Temp: 29.00 C  Humidity: 30.00 %
7
Temp: 29.00 C  Humidity: 30.00 %
8
Temp: 29.00 C  Humidity: 30.00 %
9
Temp: 29.00 C  Humidity: 30.00 %
10
Temp: 29.00 C  Humidity: 33.00 %
11
Temp: 29.00 C  Humidity: 29.00 %
12
Temp: 30.00 C  Humidity: 28.00 %
13
Temp: 30.00 C  Humidity: 28.00 %
14
Temp: 30.00 C  Humidity: 28.00 %
15
Temp: 30.00 C  Humidity: 28.00 %
16
Temp: 31.00 C  Humidity: 62.00 %
17
Temp: 34.00 C  Humidity: 26.00 %
18


"""
	
