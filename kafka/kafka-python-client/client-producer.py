# Confluence Kafka
# Document: https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})
msg = 'test'
size = 10

for _ in range(size):
    producer.produce('test-topic', msg)

producer.flush()
