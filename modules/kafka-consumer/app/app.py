from kafka import KafkaConsumer
import requests
import logging
import json

bootstrap_servers = ['kafka:9092']
topic_name = 'geolocations'

log = logging.getLogger('consumer')
logging.basicConfig(level=logging.INFO)
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    #log.info(message)
    payload = message.value
    log.info(payload)

    url = 'http://location-api:5000/api/locations'
    response = requests.post(url, json=payload)
    log.info(response)