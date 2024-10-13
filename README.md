# kafka_example

## Description

> this repository was created for the trial use of apache kafka

- 2 python clients are used as an example (`confluent-kafka` and `aiokafka`)
- Inside contains scripts for producing and consuming messages in kafka
- There is also an example of a service using confluent-kafka, and a notebook using it
- In addition to using kafka, the repository contains an example of kafka monitoring using grafana and prometheus
- I hope you find this repository useful and learn something new for yourself

## TODO

- Custom Kafka handlers (produce, consume)

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

- You can view the available commands with:

```console
make help
```

- Setup settings for docker

```console
make setup
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

### Services example

- Example of service for kafka administartion [more info in documentation](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#adminclient):

- You can try use notebooks in `./notebooks` directory

### Kafka monitoring

- Clone repository [grafana_example](https://github.com/xodiumx/grafana_example)

- Run grafana

```console
make grafana
```

- Copy example of dashboard for kafka - `./dashboards/kafka_dashboards_example.json`

- Create new dashboard

- Running a script to create data in the dashboard

```console
make kafka-loop
```
