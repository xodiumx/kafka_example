from aiokafka import AIOKafkaConsumer

from settings import settings

LOCAL_SERVER_ID = 0


async def consume_messages() -> None:
    # create consumer instance
    consumer = AIOKafkaConsumer(
        settings.KAFKA_TOPIC_NAME,
        bootstrap_servers=settings.KAFKA_HOSTS[LOCAL_SERVER_ID],
        group_id=settings.KAFKA_GROUP_ID,
    )
    # start_consume
    await consumer.start()
    try:
        # get messages from current topic
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset, msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()
