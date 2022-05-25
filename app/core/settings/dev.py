import logging

from core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev Web3 Token Registry application"

    logging_level: int = logging.DEBUG
