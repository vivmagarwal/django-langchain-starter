# Django LangChain Starter

This project is a Django starter template integrated with LangChain, using Docker and Poetry for efficient dependency management. It includes SQLite for database management in the development environment.

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

Since Python 3.10.15 is already specified, ensure that your environment is using it as the default for poetry commands. Try specifying the Python version directly in Poetry to avoid conflicts:
```
poetry env use 3.10.15
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

### Step 1: Clone the Repository

Start by cloning the repository from GitHub (or any other source) and navigate into the project directory:

```bash
git clone https://github.com/your-repo/django-langchain-starter.git
cd django-langchain-starter
```

rename `sample.env` to `.env` and update the environment variables as needed.

### Step 2: Install Python Dependencies Using Poetry

Before setting up Docker, it's recommended to install dependencies locally. You can use Poetry for this:

```bash
poetry install
```

This command will install all dependencies specified in `pyproject.toml` in your local environment.

### Step 3: Build and Start the Docker Containers

Docker Compose is used to orchestrate the running containers for the Django + Langchain project. To build and start the containers, run:

```bash
docker-compose up --build
```

This will:
- Build the Docker image.
- Start the Django web service on `http://localhost:8000`.

### Step 4: Apply Migrations

To set up the database schema for the project, apply Django migrations inside the Docker container:

```bash
docker-compose exec web poetry run python manage.py migrate
```

### Step 5: Create a Superuser

If you want to access the Django admin panel, create a superuser account:

```bash
docker-compose exec web poetry run python manage.py createsuperuser
```

Follow the prompts to create the username, email, and password.

### Step 6: Access the Running Application

Once the containers are up and running, you can access the Django application via:

```bash
http://localhost:8000
```

### Step 7: Access Django Admin Panel

To access the Django admin panel, navigate to:

```bash
http://localhost:8000/admin
```

Log in using the superuser account you created in the previous step.

---

## Useful Commands

Below is a list of useful commands to help you interact with the Docker environment and manage the Django project efficiently.

### Start Docker Containers

To start the containers without building the image again, use:

```bash
docker-compose up
```

### Stop Docker Containers

To stop the running containers, execute:

```bash
docker-compose down
```

### Access the Shell Inside the Container

If you need to access a shell inside the running web container for debugging or running commands, use:

```bash
docker-compose exec web /bin/sh
```

### Check Running Containers

To see the currently running containers:

```bash
docker ps
```

### Check Logs of Containers

To check the logs of the running `web` container:

```bash
docker-compose logs web
```

You can also check specific logs with a follow option:

```bash
docker-compose logs -f web
```

### Apply Migrations

To apply Django migrations from inside the running container:

```bash
docker-compose exec web poetry run python manage.py migrate
```

### Create a New Django App

To create a new Django app inside the container, run the following:

```bash
docker-compose exec web poetry run python manage.py startapp <app_name>
```

Replace `<app_name>` with the name of the app you wish to create.

### Running Django Management Commands

You can run any Django management command inside the container using:

```bash
docker-compose exec web poetry run python manage.py <command>
```

For example, to check the status of migrations:

```bash
docker-compose exec web poetry run python manage.py showmigrations
```

To create new migrations:

```bash
docker-compose exec web poetry run python manage.py makemigrations
```

To run unit tests:

```bash
docker-compose exec web poetry run python manage.py test
```

### Installing New Dependencies

To install new dependencies, use Poetry inside the container. Here’s how:

1. **Install a New Dependency**:  
   If you want to install a new dependency like `requests`, use the following command:

   ```bash
   docker-compose exec web poetry add requests
   ```

2. **Install Development Dependencies**:  
   To install a new development dependency, use:

   ```bash
   docker-compose exec web poetry add --dev <package-name>
   ```

3. **Rebuild the Docker Container**:  
   After adding a new dependency, you will need to rebuild your Docker image:

   ```bash
   docker-compose down
   docker-compose up --build
   ```

### Export Dependencies for Docker Environment

To export dependencies for Docker or another environment, you can use:

```bash
poetry export -f requirements.txt --output requirements.txt
```

### Update Dependencies

To update all dependencies to their latest versions, use:

```bash
docker-compose exec web poetry update
```

---

## Debugging and Troubleshooting

### Common Issues

1. **Permission Issues**:  
   If Docker or the application encounters permission issues on Linux, try running the Docker commands with `sudo` or adjust file permissions with:

   ```bash
   sudo chown -R $USER:$USER .
   ```

2. **File Not Found (`manage.py`)**:  
   If `manage.py` isn't found, ensure the Django project has been initialized with:

   ```bash
   docker-compose exec web poetry run django-admin startproject server .
   ```

3. **Container Doesn't Start**:  
   If the container fails to start, check for errors in the logs using:

   ```bash
   docker-compose logs web
   ```

4. **Dependency Issues**:  
   If you encounter dependency errors, you can regenerate the Poetry lock file and reinstall all dependencies by running:

   ```bash
   docker-compose exec web poetry lock --no-update
   docker-compose exec web poetry install
   ```

---

## Maintaining the Project

### Check for Outdated Dependencies

To check if there are any outdated dependencies in the project, use:

```bash
docker-compose exec web poetry show --outdated
```

### Accessing the Django Shell

If you want to interact with your Django project via the shell, you can run:

```bash
docker-compose exec web poetry run python manage.py shell
```

### Export the Database

You can export the database for backup purposes with the following command:

```bash
docker-compose exec web poetry run python manage.py dumpdata > db_backup.json
```

To load the backup into the database:

```bash
docker-compose exec web poetry run python manage.py loaddata db_backup.json
```

---

## Conclusion

This README covers all the steps for setting up and running the Django + Langchain project. With Docker handling the environment and Poetry managing dependencies, this project is streamlined for development and testing. Be sure to follow the steps and commands listed here to ensure smooth operation of your project.


---



# Django LangChain Starter

This project is a Django starter template integrated with LangChain. It uses Docker and Poetry for efficient dependency management, while SQLite is used for database management in development.

---

## Using the Setup

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine.
- **Docker Compose**: Comes pre-installed with Docker Desktop.
- **Poetry**: Poetry is used to manage Python dependencies.

### Steps to Run the Project

1. **Clone the Repository:**

   First, clone the repository from GitHub (or another source) and move into the project directory:

   ```bash
   git clone https://github.com/your-repo/django-langchain-starter.git
   cd django-langchain-starter
   ```

2. **Build and Start the Docker Containers:**

   To build the Docker image and start the containers, run the following command:

   ```bash
   docker-compose up --build
   ```

   - The Django application will be running on `http://localhost:8000`.

3. **Apply Migrations:**

   To set up the SQLite database, apply the Django migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create a Superuser (Optional):**

   If you want to access the Django admin panel, create a superuser:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Install or Update Dependencies:**

   If you need to install new dependencies or update existing ones, you can use **Poetry**. Follow these steps:

   - **To install a new dependency**:

     ```bash
     poetry add <package-name>
     ```

   - **To install development dependencies**:

     ```bash
     poetry add --dev <package-name>
     ```

   - **To update all dependencies to their latest versions**:

     ```bash
     poetry update
     ```

6. **Access the Application:**

   Once everything is set up, open your browser and go to `http://localhost:8000` to access the running Django app.

---

### Maintaining Dependencies

Poetry makes it easy to maintain dependencies in the project. Here are some useful commands:

- **To install all dependencies** (after cloning the repo or if `poetry.lock` changes):

  ```bash
  poetry install
  ```

- **To remove a dependency**:

  ```bash
  poetry remove <package-name>
  ```

- **To check for outdated dependencies**:

  ```bash
  poetry show --outdated
  ```

- **To export dependencies for Docker or other environments**:

  ```bash
  poetry export -f requirements.txt --output requirements.txt
  ```

---

## Creating a Similar Setup Step by Step with Explanation

### 1. **Initialize a Django Project**

   Begin by creating a new Django project:

   ```bash
   django-admin startproject server
   cd server
   ```

### 2. **Set Up Poetry for Dependency Management**

   Install Poetry from the [official website](https://python-poetry.org/docs/#installation).

   Initialize a new Poetry environment in your Django project directory:

   ```bash
   poetry init
   ```

   You can then add your necessary dependencies:

   ```bash
   poetry add django gunicorn
   ```

### 3. **Create the `Dockerfile`**

   Create a `Dockerfile` at the root of your project for containerization. This file will be used to build the Docker image:

   ```dockerfile
   # First stage: build dependencies
   FROM python:3.10-slim AS builder

   # Set the working directory
   WORKDIR /app

   # Install Poetry
   RUN pip install poetry

   # Copy Poetry files first
   COPY pyproject.toml poetry.lock ./

   # Install dependencies using Poetry
   RUN poetry config virtualenvs.create false && poetry install --no-dev

   # Second stage: final image
   FROM python:3.10-slim
   WORKDIR /app

   # Copy dependencies from the builder stage
   COPY --from=builder /app /app

   # Copy the rest of the application files
   COPY . .

   # Expose the necessary port
   EXPOSE 8000

   # Command to run the application
   CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server.wsgi"]
   ```

### 4. **Create `docker-compose.yml` for Service Orchestration**

   Docker Compose allows for easy management of services. Create a `docker-compose.yml` file to run the Django app:

   ```yaml
   version: '3'
   services:
     web:
       build: .
       command: gunicorn --bind 0.0.0.0:8000 server.wsgi
       volumes:
         - .:/app
       ports:
         - "8000:8000"
   ```

### 5. **Configure Django for SQLite**

   Update the `settings.py` file in Django to use SQLite (this should be the default in Django). If you need to ensure this setup, check the `DATABASES` section in `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

### 6. **Run the Project**

   Now you’re ready to run the project with Docker Compose:

   ```bash
   docker-compose up --build
   ```

   The Django application will be available at `http://localhost:8000`.

### 7. **Apply Migrations and Start the Server**

   Run the following commands to apply migrations and create the necessary database schema:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

### Conclusion

This setup uses Docker for environment consistency, and Poetry for easy dependency management. The setup is lightweight with SQLite for development, and the use of Docker ensures the environment is portable across machines and production stages.






```
docker run -it --rm -v $(pwd):/app codecompass django-admin startproject server .
```


# Django + Langchain Project Setup

This project sets up a Python environment using `Poetry` for dependency management, Docker for containerization, and integrates `Django` with `Langchain`. Follow the steps below to get the development environment running.

## Prerequisites


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
poetry run django-admin startproject server .
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








# Temporary VV to delete (below) rough notes






Here's an updated `README.md` that includes the useful commands, such as `poetry lock --no-update`, and a separate section for "Occasionally Used but Useful Commands."

---

# Django LangChain Starter

This project provides a Django starter template integrated with LangChain. It uses Docker and Poetry for efficient dependency management, while SQLite is used for database management in development.

---

## Using the Setup

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine.
- **Docker Compose**: Comes pre-installed with Docker Desktop.
- **Poetry**: Poetry is used to manage Python dependencies.

### Steps to Run the Project

1. **Clone the Repository:**

   First, clone the repository from GitHub (or another source) and move into the project directory:

   ```bash
   git clone https://github.com/your-repo/django-langchain-starter.git
   cd django-langchain-starter
   ```

2. **Build and Start the Docker Containers:**

   To build the Docker image and start the containers, run the following command:

   ```bash
   docker-compose up --build
   ```

   - The Django application will be running on `http://localhost:8000`.

3. **Apply Migrations:**

   To set up the SQLite database, apply the Django migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create a Superuser (Optional):**

   If you want to access the Django admin panel, create a superuser:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Install or Update Dependencies:**

   If you need to install new dependencies or update existing ones, you can use **Poetry**. Follow these steps:

   - **To install a new dependency**:

     ```bash
     poetry add <package-name>
     ```

   - **To install development dependencies**:

     ```bash
     poetry add --dev <package-name>
     ```

   - **To update all dependencies to their latest versions**:

     ```bash
     poetry update
     ```

   - **To regenerate the lock file** (if `pyproject.toml` has changed significantly):

     ```bash
     poetry lock --no-update
     ```

6. **Access the Application:**

   Once everything is set up, open your browser and go to `http://localhost:8000` to access the running Django app.

---

### Maintaining Dependencies

Poetry makes it easy to maintain dependencies in the project. Here are some useful commands:

- **To install all dependencies** (after cloning the repo or if `poetry.lock` changes):

  ```bash
  poetry install
  ```

- **To remove a dependency**:

  ```bash
  poetry remove <package-name>
  ```

- **To check for outdated dependencies**:

  ```bash
  poetry show --outdated
  ```

- **To export dependencies for Docker or other environments**:

  ```bash
  poetry export -f requirements.txt --output requirements.txt
  ```

---

## Occasionally Used but Useful Commands

1. **Regenerating the Lock File:**

   If your `pyproject.toml` has changed significantly and no longer matches the `poetry.lock` file, you can regenerate the lock file using:

   ```bash
   poetry lock --no-update
   ```

   This will ensure your `poetry.lock` file is in sync with `pyproject.toml` without updating package versions.

2. **Updating All Dependencies:**

   You can update all installed dependencies to their latest versions:

   ```bash
   poetry update
   ```

3. **Installing Dependencies Inside a Docker Container:**

   If you want to install dependencies inside a running Docker container (for testing or debugging), you can use this command:

   ```bash
   docker-compose exec web poetry install
   ```

4. **Running Shell Commands Inside the Container:**

   For executing any shell commands inside the running Docker container, use:

   ```bash
   docker-compose exec web /bin/sh
   ```

5. **Viewing Docker Container Logs:**

   If you want to inspect the logs of your running container, use:

   ```bash
   docker-compose logs web
   ```

6. **Stopping and Removing Containers:**

   If you need to stop and remove containers, networks, and volumes created by Docker Compose, use:

   ```bash
   docker-compose down
   ```

7. **Building and Rebuilding Docker Containers:**

   To force rebuild the Docker containers, use:

   ```bash
   docker-compose up --build
   ```

8. **Accessing Django Shell in the Docker Container:**

   If you need to interact with your Django project through the shell, use:

   ```bash
   docker-compose exec web python manage.py shell
   ```

---

### Conclusion

This setup uses Docker for consistent environment management, while Poetry handles Python dependencies. SQLite is used as the default database for development, and all commands related to managing dependencies and containers are provided to help streamline the development process. The additional section of occasionally used but useful commands will assist in maintaining the project and dealing with troubleshooting or container management tasks.