from kafka_service_example.services.admin import KafkaAdminService
from kafka_service_example.services.consumer import KafkaConsumerService
from kafka_service_example.services.producer import KafkaProducerService

from settings import settings

LOCAL_SERVER_ID: int = 0


def main_admin():
    admin = KafkaAdminService(
        kafka_config={"bootstrap.servers": settings.KAFKA_HOSTS[LOCAL_SERVER_ID]},
    )

    print("Creating topics:")
    print(
        admin.create_new_topics(
            topics_for_create=["test_topic_1", "test_topic_2"],
            partitions_count=3,
            repliacation_factor=1,
        )
    )

    print("Get topic info:")
    print(admin.get_topics())


def main_produce():
    KafkaProducerService()


def main_consume():
    KafkaConsumerService()
