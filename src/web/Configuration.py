import os
from pydantic import BaseSettings, AnyUrl

class Configuration(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.getenv("DATABASE_URL")

