from functools import lru_cache
from typing import Dict
from typing import Type

from app.core.settings.app import AppSettings
from app.core.settings.base import AppEnvTypes
from app.core.settings.base import BaseAppSettings
from app.core.settings.dev import DevAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
