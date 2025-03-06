from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConnectorSettings(BaseSettings):
    host: str
    port: int
    database: str
    user: str
    password: SecretStr

    model_config =SettingsConfigDict(env_file=".env.dev.pg", env_prefix="pg_")

settings = ConnectorSettings()