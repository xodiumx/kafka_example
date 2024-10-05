from enum import EnumType

from .base import KafkaAdminBase

from entities.admin import CreatedTopics, DeletedTopics, TopicsInfo


class KafkaAdminService(KafkaAdminBase):
    def get_topics(self, topic_name: str | None = None, timeout: float = 1) -> TopicsInfo:
        """
        Get information about all topics or specific topic

        Parameters:
        topic_name: topic name by default is None
                    if None get info about all topics
        timeout: float num, how long to expect a response
        """
        return TopicsInfo(topics=self._get_topics_info(topic_name=topic_name, timeout=timeout))

    def create_new_topics(
        self, topics_for_create: list, partitions_count: int, repliacation_factor: int
    ) -> CreatedTopics:
        """
        Create new topics

        Parameters:
            topics_for_create: list of topics name
            partitions_count: num of topic partiotions
            repliacation_factor: num of replication factor
        """
        return CreatedTopics(
            **self._create_new_topics(
                topics_for_create=topics_for_create,
                partitions_count=partitions_count,
                repliacation_factor=repliacation_factor,
            )
        )

    def delete_old_topics(self, topics_for_delete: list[str]) -> DeletedTopics:
        """
        Delete topics by names

        Parameters:
            topics_for_delete - list of topics name
        """
        return DeletedTopics(**self._delete_old_topics(topics_for_delete=topics_for_delete))

    def get_configs_info(self, resource_type: EnumType, resource_name: str) -> dict[str, list]:
        """
        Get config info on specific resource, available resources:
            - ANY
            - TOPIC
            - GROUP
            - BROKER
        """
        return self._get_configs_info(resource_type=resource_type, resource_name=resource_name)

    def update_configs(self): ...

    def get_groups_info(self): ...

    def describe_info(self): ...
