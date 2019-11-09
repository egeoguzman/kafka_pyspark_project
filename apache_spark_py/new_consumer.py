from pyspark import SparkContext
import time
import os
from datetime import datetime
from kafka import *
import random



mykafka = KafkaClient("10.10.10.50:9092")

producer = SimpleProducer(mykafka)

class TempData:
    def parse(self, line):
        fields = line.split(',')
        self.sensor = fields[0]
        self.timestamp = fields[1]
        self.temperature= fields[2]
        return self

    def __repr__(self):
        return 'sensor = %s, timestamp = %d, temperature = %s' % (self.sensor, self.timestamp, self.temperature)

    def to_json(self):
        return '{ "sensor":"%s", "timestamp":%d, "temperature":"%s"}'%(self.sensor, self.timestamp, self.temperature)


count = 0
sc = SparkContext(appName="spark_temperature_processor")


while 1==1:
    stationData = sc.textFile("output.txt")


    data = stationData.map(lambda x: x.split('\n')) # [u'1,2016-05-12 19:28:33.875937,36']

    split_data = data.map(lambda x: x[0].split(',')) #[u'1', u'2016-05-12 19:28:33.875937', u'36']

    joint_data_class = split_data.map(lambda x: str(x[0]) + "," + str(x[1]) + "," + str(x[2]))

    lastTime = (data.map(lambda x: x[0].split(',')).map(lambda x: str(x[1]))).collect()[-1]
    lastSensor = float((data.map(lambda x: x[0].split(',')).map(lambda x: str(x[0]))).collect()[-1])
    prevSensor = float((data.map(lambda x: x[0].split(',')).map(lambda x: str(x[0]))).collect()[-2])
    lastTemp = float((data.map(lambda x: x[0].split(',')).map(lambda x: str(x[2]))).collect()[-1])
    prevTemp = float((data.map(lambda x: x[0].split(',')).map(lambda x: str(x[2]))).collect()[-2])

    all_sensor = data.map(lambda x: x[0].split(',')).map(lambda x: float(x[0]))
    all_temp = data.map(lambda x: x[0].split(',')).map(lambda x: float(x[2]))

    i = -6
    sumOftemps = 0
    while i < -1:
        sumOftemps = sumOftemps + float((data.map(lambda x: x[0].split(',')).map(lambda x: str(x[2]))).collect()[i])
        i += 1

    avgSample = sumOftemps / 5

    sum_temp = float(all_temp.sum())
    changeRateIn5records = (lastTemp - avgSample) / 100
    change = (lastTemp - prevTemp) / 100
    print(str(prevTemp) + ">>" + str(lastTemp))
    print("Sensor State : " + str(lastSensor) + "   " + "Prev Sensor State :" + str(prevSensor))
    print("Change = %" + str(change))
    print("Change Rate In 5 Records = % " + str(changeRateIn5records))

    number_of_entries = data.count()

    avg_temp = sum_temp / number_of_entries
    timestamp = lastTime

    #data_alpha = "{\"Error Code:\"\"" + "Error 201 : Door is opened but temp is rised ... Check the Room" + "\","  + "\"timestamp\":\"" + str(timestamp) + "\"," + "\"Temp-Change\":\"" + str(change) + "\"," + "\"Last Door Situation\":\"" + str(lastSensor) + "\"" + " }"

    print("Average of last 5 record : " + str(avgSample))
    if changeRateIn5records > 0.005:
        if( lastSensor == 0):
            data_alpha = "{\"Error Code\":\"" + "Error 201 : Door is opened but temp is rised ... Check the Room!" + "\","  + "\"timestamp\":\"" + str(timestamp) + "\"," + "\"Temp-Change\":\"" + str(change) + "\"," + "\"Last Door Situation\":\"" + str(lastSensor) + "\"" + " }"
            print(data_alpha)
            producer.send_messages("alpha", data_alpha)
    if changeRateIn5records < -0.002:
        if(lastSensor == 1):
            data_alpha = "{\"Error Code\":\"" + "Door is closed but temp is low...  Check the room!" + "\","  + "\"timestamp\":\"" + str(timestamp) + "\"," + "\"Temp-Change\":\"" + str(change) + "\"," + "\"Last Door Situation\":\"" + str(lastSensor) + "\"" + " }"
            print(data_alpha)
            producer.send_messages("alpha", data_alpha)       
    if(lastSensor - prevSensor) != 0:
        print("------Attention : There is an action on the door------")
    time.sleep(3)
