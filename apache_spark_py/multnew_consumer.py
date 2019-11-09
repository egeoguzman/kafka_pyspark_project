from pyspark import SparkContext
import time
import os
from datetime import datetime
from kafka import *
import random
import requests
import json



mykafka = KafkaClient("10.10.10.50:9092")      #This Line Gives Number of Sensor and Room with GET REQUEST

producer = SimpleProducer(mykafka)
sn = requests.get('http://10.10.10.50:8081/kafka/') #Defined IP for Consumer

print("Number Of Room:" + sn.content)
cont = int(sn.content)

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

    def __repr__(self):
        return 'roomname = %s,doorstatus = %s ,sensor = %s, timestamp = %d, temperature = %s' % (self.roomname,self.doorstatus,self.sensor, self.timestamp, self.temperature)

    def to_json(self):
        return '{ "roomname":"%s","doorstatus":"%s" ,"sensor":"%s", "timestamp":"%d"," "temperature":"%s"}'%(self.roomname,self.doorstatus,self.sensor, self.timestamp, self.temperature)


count = 0
sc = SparkContext(appName="spark_temperature_processor")   #Defined Spark Context

##STARTING OUR RULES
while 1==1:
  
    stationData = sc.textFile("output.txt") ##PULLING DATA FROM OUTPUT.TXT
    

    data = stationData.map(lambda x: x.split('\n')) # EXMP: [u'1,2016-05-12 19:28:33.875937,36']
    split_data = data.map(lambda x: x[0].split(',')) #EXMP :[u'1', u'2016-05-12 19:28:33.875937', u'36']

    joint_data_class = split_data.map(lambda x: str(x[0]) + "," + str(x[1]) + "," + str(x[2]) + "," + str(x[3] + "," + str(x[4])))

    ##PARSING DATAS FROM OUTPUT.TXT LINE BY LINE ACCORDING TO ROOM NUMBER

    i = 0
    while i < cont:
        
        lastTime = (data.map(lambda x: x[0].split(',')).map(lambda x: str(x[3]))).collect()[-1]

        all_sensor = data.map(lambda x: x[0].split(',')).map(lambda x: float(x[2]))
        all_temp = data.map(lambda x: x[0].split(',')).map(lambda x: float(x[4]))
        i += 1


    ##TAKING SUM OF TEMPS FROM PARSED DATA 

    i = -cont
    sumOftemps = 0
    while i < 0:
        sumOftemps = sumOftemps + float((data.map(lambda x: x[0].split(',')).map(lambda x: str(x[4]))).collect()[i])
        i += 1
    number_of_entries = data.count()
    avgSample = sumOftemps / cont
    

    sum_temp = float(all_temp.sum())      
    
    avg_All = sum_temp / number_of_entries
    change = (avg_All - avgSample) / 100
    
    print("Avarage = " + str(avgSample))
    print("Change = %" + str(change))
    i = -cont
    x = 1

    while i < 0:
        temp_temp = float((data.map(lambda x: x[0].split(',')).map(lambda x: str(x[4]))).collect()[i])
        print("Room" + str(x)+ " = " + str(temp_temp))
        i += 1
        x += 1


    

    

    avg_temp = sum_temp / number_of_entries
    timestamp2 = lastTime

    ##CREATES JSON DATA AND SEND IT TO ANOTHER CONSUMER TO SEND DB

    data_alpha = "{\"timestamp\":\"" + str(timestamp2) + "\"," + "\"Number Of Room\":\"" + str(cont) + "\"," + "\"Temp-Change\":\"" + str(change) + "\"," + "\"Avg_Temp\":\"" + str(avgSample) + "\"" + " }"
    producer.send_messages("alpha",data_alpha)
    time.sleep(2)    
   