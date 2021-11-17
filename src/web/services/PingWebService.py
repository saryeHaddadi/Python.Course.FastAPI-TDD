from web.Configuration import Configuration
from classy_fastapi import Routable, get

class PingWebService(Routable):
    
    def __init__(self, configuration: Configuration) -> None:
        super().__init__()
        self.configuration = configuration
    
    @get("/ping")
    async def pong(self):
        print('a')
        return {
            "ping": "pong!",
            "environment": self.configuration.environment,
            "testing": self.configuration.testing
        }
