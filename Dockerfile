FROM python:3.9

# Устанавливаем библиотеки OpenGL
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем файлы
COPY . .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем статические файлы
COPY static /app/static
COPY templates /app/templates

EXPOSE 8080

CMD ["python", "main.py"]

