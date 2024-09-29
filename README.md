# kafka_example

## Application installation

- Clone repository

- Set up a virtual environment and install dependicies:

```sh
python -m venv venv
```

or

```sh
pyenv virtualenv 3.12.3 kafka_example
```

```sh
poetry install
```

- Run kafka and kafka-ui in docker
  (by default is kafka-ui from redpanda, but you can uncomment another ui or run your own.)

```sh
make kafka
```

```sh
make kafka-ui
```

> UI endpoint - http://localhost:8080/overview

- Setup environment variables

```sh
source set_env.sh
```

### Run producer and consumer examples

- Aiokafka producer and consumer run:

```sh
make aiokafka-produce
```

```sh

make aiokafka-consume
```

- Confluent-kafka producer and consumer run:

```sh
make confluent-kafka-produce
```


```sh
make confluent-kafka-consume
```

- Example of topic creation with confluent admin instance

```sh
make confluent-kafka-admin
```
