from confluent_kafka import Consumer

conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'group'}

consumer = Consumer(conf)

try:
    # consumer.subscribe('topic1')

    while True:
        msg = consumer.poll(timeout=1.0)
        print(msg)
        # if msg is None:
        #     continue

finally:
    consumer.close()
