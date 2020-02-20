#Hardware connection
#DHT11 VCC to 5v Rpi
#DHT11 GND to Gnd Rpi
#DHT11 data to 
import sys
import Adafruit_DHT
while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 18)#GPIO 18 by BCM std

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)


"""
output:-
Temp: 31.0 C  Humidity: 38.0 %
Temp: 30.0 C  Humidity: 27.0 %
Temp: 30.0 C  Humidity: 27.0 %
Temp: 30.0 C  Humidity: 27.0 %
Temp: 30.0 C  Humidity: 27.0 %
Temp: 30.0 C  Humidity: 27.0 %
Temp: 30.0 C  Humidity: 27.0 %
Temp: 30.0 C  Humidity: 27.0 %
Temp: 30.0 C  Humidity: 28.0 %
Temp: 30.0 C  Humidity: 28.0 %
Temp: 30.0 C  Humidity: 28.0 %
Temp: 30.0 C  Humidity: 28.0 %
Temp: 30.0 C  Humidity: 28.0 %
Temp: 30.0 C  Humidity: 30.0 %
Temp: 30.0 C  Humidity: 33.0 %
Temp: 30.0 C  Humidity: 33.0 %
Temp: 30.0 C  Humidity: 33.0 %
Temp: 30.0 C  Humidity: 34.0 %
Temp: 30.0 C  Humidity: 32.0 %
Temp: 31.0 C  Humidity: 32.0 %
Temp: 31.0 C  Humidity: 31.0 %
Temp: 31.0 C  Humidity: 30.0 %
Temp: 31.0 C  Humidity: 30.0 %
Temp: 31.0 C  Humidity: 30.0 %
Temp: 31.0 C  Humidity: 29.0 %
Temp: 31.0 C  Humidity: 32.0 %
Temp: 31.0 C  Humidity: 50.0 %
Temp: 31.0 C  Humidity: 55.0 %
Temp: 31.0 C  Humidity: 48.0 %
Temp: 31.0 C  Humidity: 42.0 %
Temp: 31.0 C  Humidity: 37.0 %
Temp: 31.0 C  Humidity: 34.0 %
Temp: 31.0 C  Humidity: 33.0 %
Temp: 31.0 C  Humidity: 32.0 %
Temp: 31.0 C  Humidity: 30.0 %
.
.
.

"""
