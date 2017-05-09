# it takes data from DHT11 sensor (temp and humidity) and logs the data into a csv file every 60 minutes
# measurement results can be seen in the file: data_log.csv

import os
import time 
from time import sleep 
from datetime import datetime
import Adafruit_DHT as dht

file = open("/home/pi/data_log.csv", "a")

if os.stat("/home/pi/data_log.csv").st_size == 0:
   file.write("Time,Temp,Humidity\n")
   
while True:
    t,h = dht.read_retry(dht.DHT11, 4)
    now = datetime.now()
    file.write(str(now)+","+str(h)+","+str(t)+"\n")
    file.flush()
    time.sleep(3600)

file.close()
