import os

TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["app.models.TextSummary", "aerich.models"],
            "default_connection": "default",
        },
    },
}

