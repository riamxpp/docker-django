#!/bin/sh

echo "Aguardando o banco de dados (db:5432)..."

# Tenta conectar no banco. Se falhar, espera 2 segundos e tenta de novo.
until python -c "import socket; s = socket.socket(); s.connect(('db', 5432))" 2>/dev/null; do
  echo "Banco ainda indisponível - tentando novamente..."
  sleep 2
done

echo "Banco conectado! Rodando migrações..."
python manage.py migrate

echo "Iniciando o servidor..."
python manage.py runserver 0.0.0.0:8000
