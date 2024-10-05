import logging
from enum import EnumType

from confluent_kafka.admin import AdminClient, NewTopic, ConfigResource


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
        for topic, future in fs.items():
            try:
                future.result()
                result.get("created", []).append(topic)
                logger.info(f"Topic {topic} created")
            except Exception as exc:
                result.get("not_created", []).append((topic, exc))
                logger.error(f"Failed to create topic {topic}: {exc}")
        return result

    def _delete_old_topics(self, topics_for_delete: list[str]) -> dict[str, list]:
        fs = self.admin_client.delete_topics(topics=topics_for_delete)
        result: dict[str, list] = {"deleted": [], "not_deleted": []}
        for topic, future in fs.items():
            try:
                future.result()
                result.get("deleted", []).append(topic)
                logger.info(f"Topic {topic} deleted")
            except Exception as exc:
                result.get("not_deleted", []).append((topic, exc))
                logger.error(f"Failed to delete topic {topic}: {exc}")
        return result

    def _get_configs_info(self, resource_type: EnumType, resource_name: str) -> dict[str, list]:
        fs = self.admin_client.describe_configs(
            resources=[ConfigResource(restype=resource_type, name=resource_name)],
        )
        result: dict[str, list] = {"resources": []}
        for resource, future in fs.items():
            try:
                resource_info = future.result()
                result.get("resources", []).append({resource.name: resource_info})
                logger.info(f"Resource info recivied for {resource.name}")
            except Exception as exc:
                logger.error(f"Failed to get resource info for {resource.name}: {exc}")
        return result


class KafkaProducerBase: ...


class KafkaConsumerBase: ...
