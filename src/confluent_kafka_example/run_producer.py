from confluent_kafka_example.producer import produce_messages

if __name__ == "__main__":
    produce_messages(messages_count=1_000, infinite=False)
