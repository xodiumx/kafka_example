# kafka_example

## Application installation

- Clone repository

- Set up a virtual environment and install dependicies:

```console
python -m venv venv
```

or

```console
pyenv virtualenv 3.12.3 kafka_example
```

```console
poetry install
```

- Run kafka and kafka-ui in docker
  (by default is kafka-ui from redpanda, but you can uncomment another ui or run your own.)

```console
make kafka
```

```console
make kafka-ui
```

> UI endpoint - http://localhost:8080/overview

- Setup environment variables

```sh
source set_env.sh
```

### Run producer and consumer examples

- Aiokafka producer and consumer run:

```console
make aiokafka-produce
```

```console
make aiokafka-consume
```

- Confluent-kafka producer and consumer run:

```console
make confluent-kafka-produce
```

```console
make confluent-kafka-consume
```

- Example of topic creation with confluent admin instance

```console
make confluent-kafka-admin
```
