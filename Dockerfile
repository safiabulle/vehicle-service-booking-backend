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
# (Keep everything else in your Dockerfile the same, and change the final CMD line to:)

WORKDIR /app/backend

EXPOSE 10000

CMD ["sh", "-c", "python manage.py migrate && python -m gunicorn --bind 0.0.0.0:$PORT --access-logfile - --error-logfile - config.wsgi:application"]