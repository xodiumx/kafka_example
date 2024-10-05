from .services.admin import KafkaAdminService
from .services.consumer import KafkaConsumerService
from .services.producer import KafkaProducerService


admin = KafkaAdminService()
consumer = KafkaConsumerService()
producer = KafkaProducerService()

# TODO: examples
