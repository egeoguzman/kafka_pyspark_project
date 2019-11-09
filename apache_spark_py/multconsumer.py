from kafka import KafkaConsumer
import os
from kafka import *
import time
import random
from datetime import datetime, date
import requests

sn = requests.get('http://10.10.10.50:8081/kafka/')     #This Line Gives Number of Sensor and Room with GET REQUEST
print("Number Of Room:" + sn.content)
cont = int(sn.content)
#print(['room{}'.format(i) for i in range(1, cont+1)])

consumer = KafkaConsumer(bootstrap_servers='10.10.10.50:9092',      #Defined IP for Consumer
                                 auto_offset_reset='latest')
consumer.subscribe(['room{}'.format(i) for i in range(1, cont+1)])

# !!PRODUCER -->


mykafka = KafkaClient("10.10.10.50:9092")       #Produce Datas again to consume for DB

producer = SimpleProducer(mykafka)

##PARSING PROCESSES

class TempData:                 
    def parse(self, line):
        fields = line.split(',')
        self.roomname = fields[0]
        self.doorstatus = fields[1]
        self.sensor = fields[2]
        self.timestamp = fields[3]
        self.temperature= fields[4]

        return self
    def repr(self):
        return "roomname = %s,doorstatus = %s ,sensor = %s, timestamp = %s, temperature = %s" % (self.roomname, self.doorstatus, self.sensor, self.timestamp, self.temperature)

    def to_json(self):
        return '{"roomname":%s","doorstatus":\"%s\","sensor":\"%s\","timestamp":\"%s\","temperature":"%s}' % (self.roomname,self.doorstatus,self.sensor, self.timestamp, self.temperature)



datafile = open ("output.txt", "a", 0)

#Writing to OUTPUT.TXT and CONVERTING TO JSON for data transfer

for message in consumer:
    line = str(message).split("value=")
    first_part = line[1].split("\'")
    data = first_part[1].split("\'")
    real = data[0].split("\"")
    datafile.write(real[1] + "\n")
    print(real[1])

    json_string = TempData().parse(data[0])
    json_data = json_string.to_json()
    #print(json_data)
    
    producer.send_messages("delta", json_data)  #FUNC => Produce the data