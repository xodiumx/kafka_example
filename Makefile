.PHONY: help
help:
	@echo "You need to set environment variables using the command:"
	@echo "	 source set_env.sh"
	@echo ""
	@echo "Available commands:"
	@echo "	 make kafka  -  run kafka in docker"
	@echo "	 make kafka-ui  -  run kafka UI in docker"
	@echo "	 make aiokafka-produce  -  example of produce with aiokafka"
	@echo "	 make aiokafka-consume  -  example of consume with aiokafka"
	@echo "	 make confluent-kafka-produce  -  example of produce with confluent-kafka"
	@echo "	 make confluent-kafka-consume  -  example of consume with confluent-kafka"
	@echo "	 make confluent-kafka-admin  -  example of topics create with confluent-kafka"
	@echo ""
	@echo "Service examples:"
	@echo "	 make confluent-kafka-admin-hadler - example of how administrative methods work "


.PHONY: kafka
kafka:
	docker-compose -f docker-compose-kafka.yml up -d


.PHONY: grafana
grafana:
	docker-compose -f ../grafana_example/docker-compose-grafana.yml up -d


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


.PHONY: make confluent-kafka-admin-handler
make confluent-kafka-admin-handler:
	python src/kafka_service_example/run_admin.py
