# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /achievement2

# Скачиваем/обновляем необходимые библиотеки для проекта
COPY requirements.txt /achievement2

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

RUN pip freeze

# Копируем все файлы приложения в контейнер
#COPY . .
COPY . /achievement2

# Пробрасываем порт
EXPOSE 5000

# База данных
RUN rm instance/database.db; flask db init; flask db upgrade

# Указываем команду для запуска приложения
CMD ["python", "local_start.py"]

LABEL authors="ryohoren"