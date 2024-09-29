from confluent_kafka.admin import AdminClient, NewTopic

from settings import settings

LOCAL_SERVER_ID: int = 0
NUM_OF_PARTITIONS: int = 3
NUM_OF_REPLICATION_FACTOR: int = 1


def create_new_topics(topics_for_create: list[str]) -> None:
    admin = AdminClient({"bootstrap.servers": settings.KAFKA_HOSTS[LOCAL_SERVER_ID]})

    new_topics = [
        NewTopic(topic, num_partitions=NUM_OF_PARTITIONS, replication_factor=NUM_OF_REPLICATION_FACTOR)
        for topic in topics_for_create
    ]
    # Note: In a multi-cluster production scenario, it is more typical to use a replication_factor of 3 for durability.

    # Call create_topics to asynchronously create topics. A dict
    # of <topic,future> is returned.
    fs = admin.create_topics(new_topics)

    # Wait for each operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print(f"Topic {topic} created")
        except Exception as exc:
            print(f"Failed to create topic {topic}: {exc}")
