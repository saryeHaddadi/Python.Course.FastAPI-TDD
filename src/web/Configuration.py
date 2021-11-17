import os
from typing import Optional
from pydantic import BaseSettings, AnyUrl


class Configuration(BaseSettings):
    environment: str
    testing: bool
    database_url: Optional[AnyUrl]

    @classmethod
    def get_default(self):
        return Configuration(
            environment = os.getenv("ENVIRONMENT", "dev"),
            testing = os.getenv("TESTING", 0),
            database_url = os.getenv("DATABASE_URL")
        )
