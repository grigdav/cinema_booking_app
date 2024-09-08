# Use official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project code to the container
COPY . /app/

# Expose port 8007 for the Django development server
EXPOSE 8007

# Command to run the Django development server and fill database default information
CMD ["sh", "-c", "python manage.py migrate && python manage.py db_fill && python manage.py runserver 0.0.0.0:8007"]
