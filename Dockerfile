# Use the Python slim image as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install Poetry globally
RUN pip install poetry

# Copy configuration files
COPY pyproject.toml poetry.lock ./

# Configure Poetry to avoid creating virtual environments and install dependencies
RUN poetry config virtualenvs.create false && poetry install --only main

# Copy the application files
COPY . .

# Expose the necessary port
EXPOSE 8000

# Start the application with Gunicorn via Poetry
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi"]
