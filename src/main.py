import uvicorn
from fastapi import FastAPI, Depends

from config import get_settings, Settings

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }


def main():
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)

if __name__ == '__main__':
    main()


