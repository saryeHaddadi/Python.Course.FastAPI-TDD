from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from web.services.PingWebService import PingWebService
from web.Configuration import Configuration

class ApplicationBuilder:
    def __init__(self, configuration: Configuration):
        self.app: FastAPI = None
        self.configuration = configuration
    
    def build(self):
        self.app = FastAPI()
        self.configure()
        return self.app
     
    def configure(self):
        self.configure_database()
        self.configure_routing()
        self.configure_template()
        self.configure_mounts()

    def configure_database(self):
        register_tortoise(
            self.app,
            db_url= self.configuration.database_url,
            modules={"models": ["app.models.TextSummary"]},
            generate_schemas=False,
            add_exception_handlers=True,
        )

    def configure_template(self):
        pass

    def configure_routing(self):
        self.app.include_router(PingWebService(self.configuration).router)

    def configure_mounts(self):
        pass
        
        

