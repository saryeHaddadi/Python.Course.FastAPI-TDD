#!/bin/sh
set -e

echo "Waiting for postgres..."
while ! nc -z web-db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# cd into the source code directory
cd /usr/src/app/src
exec "$@"
