# """Синхронный модуль для работы с Apache Kafka
# """

# from __future__ import annotations
# import logging
# import ssl
# import time
# from functools import wraps
# from typing import Dict, Union

# from kafka import KafkaConsumer, KafkaProducer
# from kafka.errors import KafkaError

# logger = logging.getLogger(__name__)

# REPEAT_DELAY = 3


# def kafka_handler_trier(function):  # type: ignore
#     @wraps(function)
#     def wrapper(self, *args, **kwargs):  # type: ignore
#         while True:
#             try:
#                 return function(self, *args, **kwargs)
#             except KafkaError as ex:
#                 logger.error(f"{function.__name__}(): {type(ex).__name__}: {ex}")
#                 time.sleep(self._delay)

#     return wrapper


# class KafkaHandler:
#     _consumers: Dict[str, KafkaConsumer] = {}
#     _producers: Dict[str, KafkaProducer] = {}

#     def __init__(
#         self,
#         hosts: str,
#         max_request_size: int,
#         sasl_plain_password: str = None,
#         sasl_plain_username: str = None,
#         delay: float = REPEAT_DELAY,
#     ):
#         """Инициализация

#         :param hosts: hosts Apache Kafka
#         :param max_request_size: максимальный размер сообщения
#         :param sasl_plain_password: password
#         :param sasl_plain_username: login
#         :param delay: пауза между двумя последовательными попытками kafka_handler_trier
#         """
#         self._hosts = hosts
#         self._delay = delay
#         self._sasl_plain_password = sasl_plain_password
#         self._sasl_plain_username = sasl_plain_username
#         self._max_request_size = max_request_size

#     @kafka_handler_trier
#     def push_message(self, topicname: str, message: Union[str, bytes]) -> bool:
#         """Кладет сообщение в очередь.

#         :param str topicname: Имя топика сообщений.
#         :param str message: Текст сообщения.
#         :return: True в случае успеха.
#         """
#         producer: KafkaProducer = self._producer(topicname)
#         if isinstance(message, str):
#             message = message.encode()
#         logger.info(f"Push message length = {len(message)}.")
#         producer.send(topicname, value=message)
#         return True

#     @kafka_handler_trier
#     def pop_message(self, topicname: str, consumer_group_name: str) -> str:
#         """Получает объект из очереди сообщений.
#         Чтобы закоммитить текущее положение, нужно воспользоваться
#         методом commit().

#         :param str topicname: Имя топика сообщений.
#         :param str consumer_group_name: Имя группы для консьюмера.
#         :return: Возвращает текст сообщения.
#         """
#         consumer: KafkaConsumer = self._consumer(topicname, consumer_group_name)
#         message = next(consumer).value.decode("utf-8")
#         logger.info(f"Pop message length = {len(message.value)}.")
#         return message

#     @kafka_handler_trier
#     def commit(self, topicname: str, consumer_group_name: str) -> None:
#         """Коммитит положение указателя в очереди сообщений.

#         :param str topicname: Имя топика сообщений.
#         """
#         consumer = self._consumer(topicname, consumer_group_name)
#         consumer.commit()

#     def _producer(self, topicname: str) -> KafkaProducer:
#         try:
#             return self._producers[topicname]
#         except KeyError:
#             producer = self._create_producer()
#             self._producers[topicname] = producer
#             return producer

#     def _consumer(self, topicname: str, consumer_group_name: str) -> KafkaConsumer:
#         try:
#             return self._consumers[consumer_group_name]
#         except KeyError:
#             consumer = self._create_consumer(
#                 topicname=topicname, consumer_group_name=consumer_group_name
#             )
#             self._consumers[consumer_group_name] = consumer
#             return consumer

#     @kafka_handler_trier
#     def _create_producer(self) -> KafkaProducer:
#         params = {
#             "bootstrap_servers": self._hosts,
#             "max_request_size": self._max_request_size,
#         }
#         self._authentication_apply(params)
#         producer = KafkaProducer(**params)
#         return producer

#     @kafka_handler_trier
#     def _create_consumer(self, topicname: str, consumer_group_name: str) -> KafkaConsumer:
#         params = {
#             "auto_offset_reset": "earliest",
#             "enable_auto_commit": False,
#             "bootstrap_servers": self._hosts,
#             "group_id": consumer_group_name,
#         }
#         self._authentication_apply(params)
#         return KafkaConsumer(topicname, **params)

#     def _authentication_apply(self, params):
#         if self._sasl_plain_username and self._sasl_plain_password:
#             context = ssl.create_default_context()
#             context.options &= ssl.OP_NO_TLSv1
#             context.options &= ssl.OP_NO_TLSv1_1
#             params["ssl_context"] = context
#             params["security_protocol"] = "SASL_PLAINTEXT"
#             params["sasl_mechanism"] = "PLAIN"
#             params["sasl_plain_password"] = self._sasl_plain_password
#             params["sasl_plain_username"] = self._sasl_plain_username
