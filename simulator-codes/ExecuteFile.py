import json
import time

from SimulatorFile import *
from kafka import KafkaProducer

#Eventhub Configuration
EVENTHUBS_NAMESPACE = ""
EVENT_HUB_NAME=""
CONNECTION_STRING = ""

producer = KafkaProducer(
    bootstrap_servers=[f"{EVENTHUBS_NAMESPACE}:9093"],
    security_protocol="SASL_SSL",
    sasl_mechanism="PLAIN",
    sasl_plain_username="$ConnectionString",
    sasl_plain_password=CONNECTION_STRING,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    event = generate_patient_event()
    producer.send(EVENT_HUB_NAME, event)
    print(f"Sent to Event Hub: {event}")
    time.sleep(1)