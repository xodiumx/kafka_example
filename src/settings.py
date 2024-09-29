from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    KAFKA_HOSTS: list[str]
    KAFKA_SASL_PLAIN_USERNAME: str
    KAFKA_SASL_PLAIN_PASSWORD: str
    KAFKA_MAX_REQUEST_SIZE: int
    KAFKA_FETCH_MESSAGE_MAX_BYTES: int
    KAFKA_COMPRESS: int
    KAFKA_TOPIC_PREFIX: str
    KAFKA_TOPIC_NAME: str
    KAFKA_GROUP_ID: str

    PYTHONPATH: str

    class Config:
        env_file = ".env.example"
        env_file_encoding = "utf-8"


settings = Settings()
