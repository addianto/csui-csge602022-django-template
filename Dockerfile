# Use official Python container image
FROM docker.io/library/python:3.11.5-alpine

# Configure environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# TODO: Configure environment variables required by Django project
#       e.g., database connection, parameterised configuration in settings.py

# Set the active working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the declared app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code files into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 8000

# Run the app
CMD ["/bin/sh", "-c", "python manage.py migrate && gunicorn project_django.wsgi --log-file -"]
