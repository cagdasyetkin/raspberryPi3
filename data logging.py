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
