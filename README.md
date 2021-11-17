# Tips

- To set environment variables: `System.Environment]::SetEnvironmentVariable('ENVIRONMENT','prod')`
- Container infos
    - web: docker-compose logs web
    - web-db: docker-compose exec web-db psql -U postgres

# Aerich migrations
docker-compose exec web aerich init -t db.TORTOISE_ORM -s ./src 
docker-compose exec web aerich init-db


