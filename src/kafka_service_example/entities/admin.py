from typing import Optional, Any
from pydantic import BaseModel


class PartitionInfo(BaseModel):
    id: int
    isrs: list[int]
    leader: int
    replicas: list[int]
    error: Optional[Any]


class Partition(BaseModel):
    partition_num: int
    partition_info: PartitionInfo


class TopicPartitions(BaseModel):
    partitions: list[dict[int, PartitionInfo]]


class TopicsInfo(BaseModel):
    topics: list[dict[str, TopicPartitions]]


class CreatedTopics(BaseModel):
    created: list[str]
    not_created: list
