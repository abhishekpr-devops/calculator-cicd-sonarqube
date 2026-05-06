# Calculator CI/CD with SonarCloud

Minimal Python Flask calculator API with GitHub Actions CI, SonarCloud code analysis, and Docker support.

## Features

- Flask calculator API
- Pytest unit tests
- GitHub Actions pipeline
- SonarCloud scan
- Docker image build

## API Endpoints

- GET /
- GET /health
- GET /calc?op=add&a=10&b=5
- GET /calc?op=sub&a=10&b=5
- GET /calc?op=mul&a=10&b=5
- GET /calc?op=div&a=10&b=5

## Run Locally

pip install -r requirements.txt
python app.py

## Run Tests

pytest

## Run With Docker

docker build -t calculator-app .
docker run -p 5000:5000 calculator-app

## Pipeline

Runs automatically on every push to main.
