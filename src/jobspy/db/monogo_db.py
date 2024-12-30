import os

from pymongo import MongoClient
from pymongo.synchronous.database import Database

from jobspy import create_logger


class MongoDB:
    _instance = None
    db:Database = None
    def __new__(cls):

        if cls._instance is not None:
            return cls._instance

        self = super().__new__(cls)
        cls._instance = self
        logger = create_logger("Mongo Client")
        mongoUri = os.getenv("MONGO_URI")
        if not mongoUri:
            logger.error("MONGO_URI environment variable is not set")
            raise ValueError("MONGO_URI environment variable is not set")
        client = MongoClient(mongoUri)
        database_name = os.getenv("MONGO_DB_NAME")
        if not database_name:
            logger.error("MONGO_DB_NAME environment variable is not set")
            raise ValueError(
                "MONGO_DB_NAME environment variable is not set")

        self.db = client[database_name]
        return cls._instance