# devops-pipeline-automation

# Steps to Run Lint Check Locally

1. Install flake8 (Recommended: Inside a virtual environment): pip install flake8

2. Run flake8 on specific files or directories: flake8 scripts/

3. Or for a specific file: flake8 scripts/generator.py

# Steps to Run test Check Locally

1. Activate virtual environment (if not already active): source venv/bin/activate
   
2. Install pytest (if not already installed): pip install pytest

3. Run pytest on the entire tests/ directory: pytest tests/

4. Or run pytest on a specific test file: pytest tests/test_generator.py

5. View the test output:
Pytest will display which tests passed or failed with a summary.

# Steps to deploy the application

1. Make sure Docker is installed and running.

2. Log in to Docker Hub: docker login -u <your-docker-username>

3. Build the Docker image: docker build -t <your-docker-username>/<your-repo-name>:latest .
   
4. Push the Docker image to Docker Hub: docker push <your-docker-username>/<your-repo-name>:latest
