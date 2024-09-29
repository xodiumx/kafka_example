from confluent_kafka_example.admin import create_new_topics

if __name__ == "__main__":
    create_new_topics(topics_for_create=["test-topic1", "test-topic2"])
