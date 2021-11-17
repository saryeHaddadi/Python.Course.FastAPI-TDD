from web.services.base.BaseWebService import BaseWebService
from classy_fastapi import get

class PingWebService(BaseWebService):
    
    def __init__(self, configuration: BaseWebService):
        super().__init__(configuration)
    
    @get("/ping")
    async def pong(self):
        return {
            "ping": "pong!",
            "environment": self.configuration.environment,
            "testing": self.configuration.testing
        }
