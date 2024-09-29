.PHONY: kafka
kafka:
	docker-compose -f docker-compose-kafka.yml up -d

.PHONY: kafka-ui
kafka-ui:
	docker-compose -f docker-compose-kafka-ui.yml up -d


.PHONY: aiokafka-produce
aiokafka-produce:
	python src/aiokafka_example/run_producer.py


.PHONY: aiokafka-consume
aiokafka-consume:
	python src/aiokafka_example/run_consumer.py


.PHONY: confluent-kafka-produce
confluent-kafka-produce:
	python src/confluent_kafka_example/run_producer.py


.PHONY: confluent-kafka-consume
confluent-kafka-consume:
	python src/confluent_kafka_example/run_consumer.py


.PHONY: confluent-kafka-admin
confluent-kafka-admin:
	python src/confluent_kafka_example/run_admin.py
