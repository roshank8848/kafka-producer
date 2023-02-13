from confluent_kafka import Producer
import random
import time
from uuid import uuid4
import json

locdata_car0 = """ {"lat":{apple},"lang":"60.30","speed":"30"}"""
locdata_car1 = """ {"lat":"80.40","lang":"60.50","speed":"40"}"""
locdata_car2 = """ {"lat":"80.30","lang":"60.20","speed":"80"}"""

locdata_car0_json = locdata_car0.encode()
locdata_car1_json = locdata_car1.encode()
locdata_car2_json = locdata_car2.encode()

def delivery_report(err,msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} partition [{}] offset {}'.format(msg.topic(), msg.partition(),msg.offset()))

conf = {
    'bootstrap.servers':'kafka:9094',
    'client.id':'python-producer-01'
}

producer = Producer(conf)
topic = 'my-topic'
#producer.poll(0)
car_ids = ['car-1','car-2','car-3','car-4','car-5','car-6','car-7']

while True:
    for car_id in car_ids:
        print(car_id)
        partition_key = hash(car_id)
        producer.produce(topic,key=car_id.encode('utf-8'),value=locdata_car0_json,callback=delivery_report)
        producer.flush()
    time.sleep(1)