from fastapi import FastAPI
from loguru import logger

from app.core.settings.app import AppSettings
from app.db import db


async def connect_to_db(app: FastAPI, settings: AppSettings) -> None:
    logger.info("Connecting to PostgreSQL")
    db.connect()

    logger.info("Creating tables")
    db.create_tables([])

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await db.close()

    logger.info("Connection closed")
