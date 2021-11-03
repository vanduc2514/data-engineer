# Confluence Kafka
# Document: https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})
msg = ('kafka_test' * 20).encode()[:100]
print(msg)
size = 10

#
# def delivery_report(err, decoded_message, original_message):
#     if err is not None:
#         print(err)
for _ in range(size):
    producer.produce('topic1', msg)

producer.flush()
