from confluent_kafka import Consumer
from confluent_kafka.cimpl import Message

from settings import settings

LOCAL_SERVER_ID: int = 0
KAFKA_MESSAGE_POLLING: float = 1.0


def consume_messages() -> None:
    consumer = Consumer(
        {
            "bootstrap.servers": settings.KAFKA_HOSTS[LOCAL_SERVER_ID],
            "group.id": settings.KAFKA_GROUP_ID,
            "auto.offset.reset": "earliest",
        }
    )

    consumer.subscribe([settings.KAFKA_TOPIC_NAME])

    while True:
        msg: Message = consumer.poll(KAFKA_MESSAGE_POLLING)

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        print(f"Received message: {msg.value()}")

    consumer.close()
