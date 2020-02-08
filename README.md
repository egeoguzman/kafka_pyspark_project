Real Time Data Streaming and Analyzing with Apache Kafka & PySpark </br>

# Complete Hadoop Project with Kafka-Pyspark-MongoDB

## What is Kafka?

Apache Kafka® is a distributed streaming platform. Kafka is used for building real-time
streaming data pipelines that reliably get data between systems or applications or building real-
time streaming applications that transform or react to the streams of data. Like many publish-
subscribe messaging systems, Kafka maintains feeds of messages in topics. Producers write data
to topics and consumers read from topics. Since Kafka is a distributed system, topics are
partitioned and replicated across multiple nodes.

- **Topics:** A topic is a category or feed name to which records are published. Topics in Kafka
    are always multi-subscriber; that is, a topic can have zero, one, or many consumers that
    subscribe to the data written to it.
- **Producers:** Producers publish data to the topics of their choice. The producer is
    responsible for choosing which record to assign to which partition within the topic. This
    can be done in a round-robin fashion simply to balance load or it can be done according
    to some semantic partition function
- **Consumers:** Consumers label themselves with a consumer group name, and each record
    published to a topic is delivered to one consumer instance within each subscribing
    consumer group. Consumer instances can be in separate processes or on separate
    machines.

#### What makes Kafka unique?

Kafka treats each topic partition as a log (an ordered set of messages). Each message in a
partition is assigned a unique offset. Kafka does not attempt to track which messages were read
by each consumer and only retain unread messages; rather, Kafka retains all messages for a set
amount of time, and consumers are responsible to track their location in each log. Consequently,
Kafka can support a large number of consumers and retain large amounts of data with very little
overhead.

**Download address** : https://www.apache.org/dyn/closer.cgi?path=/kafka/2.2.0/kafka_2.12-2.2.0.tgz

## What is Zookeeper?

Apache Zookeeper is an open source distributed coordination service that helps you
manage a large set of hosts. Management and coordination in a distributed environment are
tricky. Zookeeper automates this process and allows developers to focus on building software
features rather worry about the distributed nature of their application.

Zookeeper helps you to maintain configuration information, naming, group services for
distributed applications. It implements different protocols on the cluster so that the application
should not implement on their own. It provides a single coherent view of multiple machines.

**Download address** : https://www.apache.org/dyn/closer.cgi/zookeeper/


## Let’s Start

### Step 1:

#### Download the 2.2.0 release and un-tar it.

> tar -xzf kafka_2.12-2.2.0.tgz

> cd kafka_2.12-2.2.

### Step 2:

Kafka uses ZooKeeper so you need to first start a ZooKeeper server

> bin/zookeeper-server-start.sh config/zookeeper.properties

Now start the Kafka server:

> bin/kafka-server-start.sh config/server.properties

### STEP 3:

Let's create a topic named "test" with a single partition

> bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --
topic test

### STEP 4:

Send some messages. Run the producer and then type a few messages into the console to send
to the server.

> bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

This is a message

This is another message

### STEP 5:

Kafka also has a command line consumer that will dump out messages to standard output

> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

This is a message

This is another message


## What is Spark (Pyspark)?

Spark is a general-purpose distributed data processing engine that is suitable for use in a
wide range of circumstances. On top of the Spark core data processing engine, there are libraries
for SQL, machine learning, graph computation, and stream processing, which can be used
together in an application. Programming languages supported by Spark include: Java, Python,
Scala, and R. Application developers and data scientists incorporate Spark into their applications
to rapidly query, analyze, and transform data at scale. Tasks most frequently associated with
Spark include ETL and SQL batch jobs across large data sets, processing of streaming data from
sensors, IoT, or financial systems, and machine learning tasks.

### STEP 1:

Install Python

### STEP 2:

Download & Install Spark with pip

> pip install pyspark

### STEP 3:

Your ~/.bash_profile file should be like that;

## What is MongoDB?

MongoDB is a document-oriented NoSQL database used for high volume data storage which
instead of having data in a relational type format, it stores the data in documents. MongoDB is a
database which came into light around the mid-2000s. It falls under the category of a NoSQL
database.

Download from https://www.mongodb.com/download-center


## LET’S START CODING

### Step 1:

Configure your zoo.cfg from Zookeeper/conf

Set a dir for zookeeper data with “dataDir=” line

Default Zookeeper port is 2181

### Step 2:

Start zookeeper with

> bin/zookeeper-server-start.sh config/zookeeper.properties


### Step 3:

Configure your settings for Kafka server in kafka_2.12-2.2.0\config\server.properties

Set your Listener : “listeners=PLAINTEXT://localhost:9092”

And start server with bin/kafka-server-start.sh config/server.properties

### Step 4:

Unzip KafkaProducer.zip and run SipringBootKafkaProducerExampleApplication.java to start
Producer.

UserResource.java generates random values for Book object and sends it to the Topic.

### Step 5:

Unzip test.zip and run test.java

This script ask you to number of rooms to simulate sensors and sent to Producer with a HTTP
GET.

This HTTP GET Request makes UserResource.java run continuously.


### Step 6:

Run multconsumer.py with

_> python multconsumer.py_



### Part 7:

We have to run consumerAll.py with

> python consumerAll.py

To send incoming message to the database from kafka which produced by multconsumer.py.

### Part 8:

Run Multnew_consumer.py to process incoming data from a text file and produces data about
changes and averages of temperatures.

Sends this data to alpha topic to be consumed by consumerAct.py



### PART 9:

We have to run consumerAct.py with

> python consumerAct.py

To send incoming message to the database from kafka which produced by
multnew_consumer.py

## Conclusion:

As you can see ,we can analyze and scale real-time streaming with Spark. Also we use Apache
Kafka to send this data or to encrypt topics , to create and edit message queues.



PLEASE CHECK IT OUT!!! </h3>
