# Kafka Producer

The kafka produces messages to `my-topic` topic. The car id is used as a partition key. The message beloning to a car would be sent to the same partition based on partition key. To run the app on the development setup. 

## Install requirements

```bash
pip install -r requirements.txt
```

## Execute the command for running the consumer

```bash
python producer.py
```

## Building a docker container

```bash
docker build -t kafka-producer:0.0.1 .
```

## Note
Use appropriate kafka brokers and topics for the producer code to work.