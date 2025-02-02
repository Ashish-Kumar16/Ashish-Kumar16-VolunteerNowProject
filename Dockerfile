# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the container
COPY . /app/

# Set environment variables (optional)
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=myproject.settings.production  # Adjust for your project settings

# Expose the port the app will run on
EXPOSE 8000

# Collect static files (needed for production)
RUN python manage.py collectstatic --noinput

# Command to run the application using Gunicorn
CMD ["gunicorn", "volunteernow.wsgi:application", "--bind", "0.0.0.0:8000"]
