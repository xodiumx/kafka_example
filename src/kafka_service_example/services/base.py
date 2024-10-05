import logging

from confluent_kafka.admin import AdminClient, NewTopic


logger = logging.getLogger(__name__)


class KafkaAdminBase:
    def __init__(
        self,
        kafka_config: dict,
    ) -> None:
        self.admin_client = AdminClient(conf=kafka_config)

    def _get_topics_info(self, topic_name: str | None, timeout: float):
        topics = self.admin_client.list_topics(topic_name, timeout=timeout).topics
        result = []
        for topic_name, topic in topics.items():
            result.append(
                {
                    topic_name: {
                        "partitions": [
                            {
                                partition_num: {
                                    "id": partition.id,
                                    "isrs": partition.isrs,
                                    "leader": partition.leader,
                                    "replicas": partition.replicas,
                                    "error": partition.error,
                                }
                                for partition_num, partition in topic.partitions.items()
                            }
                        ]
                    }
                }
            )
        return result

    def _create_new_topics(
        self, topics_for_create: list, partitions_count: int, repliacation_factor: int
    ) -> dict[str, list]:
        new_topics = [
            NewTopic(topic, num_partitions=partitions_count, replication_factor=repliacation_factor)
            for topic in topics_for_create
        ]
        fs = self.admin_client.create_topics(new_topics)
        result: dict[str, list] = {"created": [], "not_created": []}
        for topic, f in fs.items():
            try:
                f.result()
                result.get("created", []).append(topic)
                logger.info(f"Topic {topic} created")
            except Exception as exc:
                result.get("not_created", []).append((topic, exc))
                logger.error(f"Failed to create topic {topic}: {exc}")
        return result


class KafkaProducerBase: ...


class KafkaConsumerBase: ...
