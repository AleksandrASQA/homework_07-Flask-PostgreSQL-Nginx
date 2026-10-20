# Базовый образ Python
FROM python:3.10-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . .

# Открываем порт (Gunicorn будет слушать его)
EXPOSE 8000

# Команда запуска: Gunicorn обслуживает Flask приложение
# workers=3 - количество рабочих процессов
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "app:app"]