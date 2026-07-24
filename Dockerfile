FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Copy requirements and install them globally in the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# If your manage.py is inside a 'backend' folder, adjust this. 
# (If your manage.py is right in the root folder, remove the 'backend/' part below)
WORKDIR /app/backend

EXPOSE 10000

# Explicitly use python -m gunicorn to ensure it finds the package
CMD ["sh", "-c", "python -m gunicorn --bind 0.0.0.0:$PORT config.wsgi:application"]