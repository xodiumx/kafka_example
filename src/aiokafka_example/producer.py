import orjson

from aiokafka import AIOKafkaProducer

from settings import settings


async def produce_messages():
    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_HOSTS,
    )
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        for i in range(1_000):
            await producer.send_and_wait(settings.KAFKA_TOPIC_NAME, orjson.dumps(f"Message {i}"))
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
