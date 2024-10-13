.PHONY: help
help:
	@echo "You need to set environment variables using the command:"
	@echo "	 source set_env.sh"
	@echo "	 make setup  -  setup docker settings"
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
	@echo "Grafana monitoring:"
	@echo "	 make grafana  -  clones the repository before launching it, and after use this command for start grafana"
	@echo "  make kafka-loop  -  infinite data produce for dashboard charts"


.PHONY: setup
setup:
	docker network create grafana_example_default


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


.PHONY: kafka-loop
kafka-loop:
	python src/confluent_kafka_example/run_loop.py
