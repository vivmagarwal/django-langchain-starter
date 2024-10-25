# Use the official Python slim image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy Poetry configuration files from the backend directory
COPY pyproject.toml poetry.lock ./

# Install Poetry globally
RUN pip install poetry

# Configure Poetry and install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the rest of the application code
COPY . .

# Expose the necessary port
EXPOSE 8000

# Start the application with Gunicorn
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi"]
