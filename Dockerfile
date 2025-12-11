FROM python:3.10-slim

# Prevent interactive prompts
ENV PYTHONUNBUFFERED 1

# Create working directory
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
  gcc \
  build-essential \
  libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
