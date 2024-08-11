from aiokafka import AIOKafkaProducer
import asyncio
import orjson

async def send_one():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:29092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        for i in range(1_000):
            await producer.send_and_wait("my_topic", orjson.dumps(f"Message {i}"))
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

asyncio.run(send_one())

