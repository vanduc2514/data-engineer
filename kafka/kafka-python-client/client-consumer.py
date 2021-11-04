# Doc: https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html

from confluent_kafka import Consumer

conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'test-group'}

consumer = Consumer(conf)

try:
    consumer.subscribe(["test-topic"])

    while True:
        msg = consumer.poll(timeout=1.0)
        print(msg)

finally:
    consumer.close()
