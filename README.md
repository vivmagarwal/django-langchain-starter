# Django + Langchain Project Setup

This project sets up a Python environment using `Poetry` for dependency management, Docker for containerization, and integrates `Django` with `Langchain`. Follow the steps below to get the development environment running.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** (with Docker Compose)
- **Python 3.10.x** (managed with `pyenv` or installed locally)
- **Poetry** (installed with `pipx`)

### 1. Install `pyenv` to Manage Python Versions

To ensure you are using the correct Python version (3.10.15), you should install `pyenv`.

Run the following command to install `pyenv`:

```bash
curl https://pyenv.run | bash
```

Configure your shell (add these lines to your `~/.bashrc` or `~/.zshrc`):

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Restart your terminal and verify installation:

```bash
pyenv --version
```

### 2. Install Python 3.10.15

Once `pyenv` is installed, run these commands to install Python 3.10.15 and set it as your local version for the project:

```bash
pyenv install 3.10.15
pyenv local 3.10.15
```

Verify your Python version:

```bash
python --version
```

### 3. Install `pipx` to Manage CLI Tools

`pipx` allows you to install and run Python applications in isolated environments.

Run the following command to install `pipx`:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Verify installation:

```bash
pipx --version
```

### 4. Install `Poetry` using `pipx`

Use `pipx` to install `Poetry`, the tool that will manage project dependencies:

```bash
pipx install poetry
```

Verify `Poetry` is installed:

```bash
poetry --version
```

## Project Setup

With the prerequisites installed, you can now set up your project.

### 5. Clone the Repository

If this project is hosted in a repository, clone it locally:

```bash
git clone <your-repository-url>
cd <your-project-directory>
```

### 6. Initialize Django Project (If Not Already Done)

If a `manage.py` file is missing, you need to initialize the Django project. You can run the following command to create it:

```bash
poetry run django-admin startproject mysite .
```

This will generate the `manage.py` file and the basic Django project structure.

### 7. Install Project Dependencies

With the `pyproject.toml` and `poetry.lock` files already configured, you can install all project dependencies by running:

```bash
poetry install
```

This will install all the necessary dependencies for Django, Langchain, and other packages listed in the `pyproject.toml`.

### 8. Use the Virtual Environment

To work inside the virtual environment created by Poetry, run:

```bash
poetry shell
```

This will activate the environment where all dependencies are installed and managed.

### 9. Run Database Migrations

Ensure the database is set up correctly by applying the initial migrations:

```bash
poetry run python manage.py migrate
```

### 10. Create a Superuser (for Django Admin)

If you want to access the Django admin interface, create a superuser:

```bash
poetry run python manage.py createsuperuser
```

Follow the prompts to set up the username, email, and password.

## Docker Setup and Usage

### 11. Build the Docker Containers

Now that everything is set up locally, you can build the Docker container to run the application. Ensure Docker is running, then run:

```bash
docker-compose build
```

### 12. Run the Containers

To start the containers and run the application, use the following command:

```bash
docker-compose up
```

This will launch the Django development server on `http://localhost:8000`. You can access the Django Admin by navigating to `http://localhost:8000/admin`.

To run the containers in detached mode (in the background), use:

```bash
docker-compose up -d
```

### 13. Access the Running Container

If you need to access the running container for debugging or checking logs, use:

```bash
docker-compose exec web bash
```

### 14. Stop the Containers

To stop the Docker containers, run:

```bash
docker-compose down
```

This will stop and remove all running containers.

## Development Workflow

### 15. Running Django Commands

You can run any Django management command inside the Docker container using the `poetry` environment. For example, to check the status of migrations:

```bash
docker-compose exec web poetry run python manage.py showmigrations
```

To make new migrations:

```bash
docker-compose exec web poetry run python manage.py makemigrations
```

### 16. Running Unit Tests

If you have set up Django tests, you can run them inside the Docker container:

```bash
docker-compose exec web poetry run python manage.py test
```

### 17. Installing New Dependencies

To install new dependencies, use `poetry`:

```bash
poetry add <package-name>
```

After adding the dependency, don’t forget to rebuild your Docker image:

```bash
docker-compose down
docker-compose build
docker-compose up
```

## Troubleshooting

### Common Issues

- **File Not Found (`manage.py`)**: Ensure you've run the command to initialize the Django project (`django-admin startproject`) and check that the file exists in the project root.
- **Permission Issues**: Ensure Docker has the necessary permissions to access the project files. On Linux/Mac, use `sudo` if needed.
- **Dependency Errors**: If any dependency issues arise, you can update the `poetry.lock` file using:
  
  ```bash
  poetry lock --no-update
  poetry install
  ```

## Conclusion

This README provides a complete guide to setting up, running, and managing the Django + Langchain project with Docker and Poetry. Following these steps will ensure you have a smooth development environment, leveraging the power of containerization and dependency management.
