import asyncio

from aiokafka_example.consumer import consume_messages

if __name__ == "__main__":
    asyncio.run(consume_messages())
