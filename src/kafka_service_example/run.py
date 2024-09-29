# import orjson

# from kafka_service_example.kafka_hadler import KafkaHandler

# from settings import settings


# def main():
#     kafkahandler = KafkaHandler(
#         hosts=settings.KAFKA_HOSTS,
#         max_request_size=settings.KAFKA_MAX_REQUEST_SIZE,
#         sasl_plain_password=settings.KAFKA_SASL_PLAIN_PASSWORD,
#         sasl_plain_username=settings.KAFKA_SASL_PLAIN_USERNAME,
#     )


#     kafkahandler.push_message("test_topic", orjson.dumps({"test_key": "test123"}))


# if __name__ == "__main__":
#     main()
