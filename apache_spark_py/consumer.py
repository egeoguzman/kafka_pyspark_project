from kafka import KafkaConsumer
import os

consumer = KafkaConsumer(bootstrap_servers='10.10.10.50:9092',
                                 auto_offset_reset='latest')
consumer.subscribe(['test'])


class TempData:
	def parse(self, line):
		fields = line.split(',')
		self.sensor = fields[0]
		self.timestamp = fields[1]
		self.temperature= fields[2]

		return self
	def __repr__(self):
		return "sensor = %s, timestamp = %s, temperature = %s" % (self.sensor, self.timestamp, self.temperature)

	def to_json(self):
		return '{"sensor":%s","timestamp":\"%s\","temperature":"%s}'%(self.sensor, self.timestamp, self.temperature)



datafile = open ("output.txt", "a", 0)
jsonfile = open ("tempJson.json", "a+", 0)


for message in consumer:
	line = str(message).split("value=")
	first_part = line[1].split("\'")
	data = first_part[1].split("\'")
	real = data[0].split("\"")
	datafile.write(real[1] + "\n")
	print(real[1])


	
#	 json_string = TempData().parse(data[0])
#	 json_data = json_string.to_json()
#	 print(json_data)


#	 if os.path.getsize("tempJson.json"):
#	 	jsonfile.seek(-1, os.SEEK_END) #remove the last ]
#	 	jsonfile.truncate()
#	 	jsonfile.write(",\n")
#	 	jsonfile.write(json_data)
#	 	jsonfile.write("]")
#	 else:
#	 	jsonfile.write("[")
#	 	jsonfile.write(json_data + "\n")
