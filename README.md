# marvel-character-db
Marvel Character Database App
Marvel App Code Files*
We'll use Python and Flask framework. Create these files in your local project folder:

This is a sample DevOps project that showcases a CI/CD pipeline using Jenkins for a Python Flask API serving Marvel character data. It includes automated testing, Docker containerization, and deployment to AWS EC2.

## Features
- Flask API with multiple endpoints
- Pytest unit testing
- Docker containerization
- CI/CD pipeline via Jenkins
- Deployment automation with AWS EC2

## Endpoints
- `/` – Home route
- `/characters` – List all characters
- `/characters/<name>` – Get character by name

## Usage
Build and run locally:
```bash
docker build -t marvel-api.
docker run -p 5000:5000 marvel-api
```

Run tests:
```bash
pytest tests/
```

## Author
Sernaggio Blaise
```
