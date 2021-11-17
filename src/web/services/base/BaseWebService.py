from web.Configuration import Configuration
from classy_fastapi import Routable

class BaseWebService(Routable):
    
    def __init__(self, configuration: Configuration) -> None:
        super().__init__()
        self.configuration = configuration
    
