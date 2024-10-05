from .base import KafkaAdminBase

from entities.admin import CreatedTopics, DeletedTopics, TopicsInfo


class KafkaAdminService(KafkaAdminBase):
    def get_topics(self, topic_name: str | None = None, timeout: float = 1) -> TopicsInfo:
        """
        Get information about all topics or specific topic
        """
        return TopicsInfo(topics=self._get_topics_info(topic_name=topic_name, timeout=timeout))

    def create_new_topics(
        self, topics_for_create: list, partitions_count: int, repliacation_factor: int
    ) -> CreatedTopics:
        return CreatedTopics(
            **self._create_new_topics(
                topics_for_create=topics_for_create,
                partitions_count=partitions_count,
                repliacation_factor=repliacation_factor,
            )
        )

    def delete_old_topics(self, topics_for_delete) -> DeletedTopics:
        return DeletedTopics(**self._delete_old_topics(topics_for_delete=topics_for_delete))

    def update_partitions(self): ...

    def get_configs_info(self): ...

    def update_configs(self): ...

    def get_groups_info(self): ...

    def describe_info(self): ...
