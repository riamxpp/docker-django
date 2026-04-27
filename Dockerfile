# 1. Use uma imagem oficial do Python
FROM python:3.11-slim

# 2. Define variáveis de ambiente para o Python
# Evita que o Python gere arquivos .pyc e garante que o output vá direto para o console
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Define o diretório de trabalho dentro do contêiner
WORKDIR /code

# 4. Instala dependências do sistema necessárias para o psycopg2 (driver do Postgres)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Instala as dependências do Python
# Copiamos primeiro apenas o requirements para aproveitar o cache do Docker
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Copia o restante do código do projeto
COPY . /code/

COPY entrypoint.sh /code/
ENTRYPOINT ["/code/entrypoint.sh"]
