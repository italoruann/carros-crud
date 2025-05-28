#!/bin/sh

set -e

echo "--- Verificando o status das migrações (antes de aplicar) ---"
python manage.py showmigrations

echo "--- Aplicando as migrações do banco de dados ---"
python manage.py migrate

echo "--- Status das migrações (após aplicar) ---"
python manage.py showmigrations

echo "--- Iniciando o servidor Django ---"

exec python manage.py runserver 0.0.0.0:8000