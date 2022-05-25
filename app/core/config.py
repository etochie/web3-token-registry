from functools import lru_cache
from typing import Dict
from typing import Type

from core.settings.app import AppSettings
from core.settings.base import AppEnvTypes
from core.settings.base import BaseAppSettings
from core.settings.dev import DevAppSettings
from core.settings.prod import ProdAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
