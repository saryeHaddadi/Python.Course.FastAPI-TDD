import os

# Used just for the first DB initialization
# docker-compose exec web aerich init -t app.db.TORTOISE_ORM
TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["app.models.TextSummary", "aerich.models"],
            "default_connection": "default",
        },
    },
}

