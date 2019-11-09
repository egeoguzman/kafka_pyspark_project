from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import json


##THIS CONSUMER TAKES EVERY TYPE OF DATA PROCESSED AND DIVIDED AND SEND THEM TO DB COLLECTION

consumer2 = KafkaConsumer(
    'alpha',            ##TOPIC THAT CONTAINS DIVIDED AND PROCCESED DATA
     bootstrap_servers=['10.10.10.50:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


client2 = MongoClient('localhost:27017')             ##CONNECTS Mongodb client
collection2 = client2.admin.Activities


for message2 in consumer2:              ##TAKES MASSAGES AS A DATA AND SEND IT TO DB ONE-BY-ONE
    message2 = message2.value
    #print(message2)
    collection2.insert_one(message2)
    print('{} added to {}'.format(message2, collection2))
