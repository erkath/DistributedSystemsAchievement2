# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /achievement2

RUN apt-get update -y && \
    apt-get install -y pkg-config python3-dev default-libmysqlclient-dev build-essential

# Скачиваем/обновляем необходимые библиотеки для проекта
COPY requirements.txt /achievement2

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt && \
    pip freeze

# Копируем все файлы приложения в контейнер
#COPY . .
COPY . /achievement2

# Пробрасываем порт
EXPOSE 5000

LABEL authors="ryohoren"

ENTRYPOINT ["/bin/bash", "/achievement2/scripts/entrypoint.sh"]