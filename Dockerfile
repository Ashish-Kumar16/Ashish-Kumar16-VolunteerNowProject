# Use an official Python image (slim version for smaller size)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (e.g., required for PostgreSQL, Pillow, etc.)
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies inside a virtual environment
RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=volunteernow.settings.production \
    PATH="/venv/bin:$PATH"

# Expose the application port
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Apply database migrations
RUN python manage.py migrate

# Switch to a non-root user (security best practice)
RUN useradd --create-home django_user
USER django_user

# Command to run the application using Gunicorn
CMD ["gunicorn", "volunteernow.wsgi:application", "--bind", "0.0.0.0:8000"]
