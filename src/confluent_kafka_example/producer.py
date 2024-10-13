import time
import random

import orjson

from confluent_kafka import Producer
from confluent_kafka.cimpl import Message

from settings import settings

LOCAL_SERVER_ID: int = 0


def delivery_report(err, msg: Message) -> None:
    """
    Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush().
    """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message {msg.value()} delivered to: \ntopic - {msg.topic()} \npartition - [{msg.partition()}]")


def produce_messages(messages_count: int, infinite: bool) -> None:
    """
    Test kafka producer
    """
    producer = Producer({"bootstrap.servers": settings.KAFKA_HOSTS[LOCAL_SERVER_ID]})

    if infinite:
        i = 0
        while True:
            time.sleep(random.random())
            producer.poll(0)
            producer.produce(settings.KAFKA_TOPIC_NAME, orjson.dumps(f"Message {i}"), callback=delivery_report)
            i += 1

    for i in range(messages_count):
        # Trigger any available delivery report callbacks from previous produce() calls
        producer.poll(0)

        # Asynchronously produce a message. The delivery report callback will
        # be triggered from the call to poll() above, or flush() below, when the
        # message has been successfully delivered or failed permanently.
        producer.produce(settings.KAFKA_TOPIC_NAME, orjson.dumps(f"Message {i}"), callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    producer.flush()
