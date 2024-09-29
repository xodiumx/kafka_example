import asyncio

from aiokafka_example.producer import produce_messages

if __name__ == "__main__":
    asyncio.run(produce_messages())
