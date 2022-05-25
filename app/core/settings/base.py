import os
from enum import Enum
from pydantic import BaseSettings


class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = os.getenv('ENV')

    class Config:
        env_file = ".env"
