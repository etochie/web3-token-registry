import logging

from core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    debug: bool = False

    title: str = "Prod Web3 Token Registry application"

    logging_level: int = logging.INFO
