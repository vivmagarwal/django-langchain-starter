# Use an official Python runtime as a parent image
FROM python:3.10.15-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project metadata
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install poetry==1.8.3
RUN poetry install --no-dev --no-interaction

# Copy all project files to the container
COPY . /app

# Expose port 8000 for Django
EXPOSE 8000

# Start the Django development server (referencing manage.py)
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
