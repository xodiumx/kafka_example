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
