# Calculator API CI/CD Pipeline

A minimal Python Flask calculator API deployed using a DevOps pipeline.

This project demonstrates:

- GitHub source control
- GitHub Actions CI pipeline
- Pytest automated testing
- SonarCloud code quality scan
- Docker image build
- DockerHub image push
- AWS EC2 container deployment

---

## Tech Stack

| Area | Tool |
|---|---|
| Language | Python |
| Framework | Flask |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Code Quality | SonarCloud |
| Containerization | Docker |
| Registry | DockerHub |
| Deployment | AWS EC2 |
| OS | Ubuntu |

---

## Architecture

```text
Code
  ↓
GitHub Repository
  ↓
GitHub Actions
  ↓
Pytest
  ↓
SonarCloud
  ↓
Docker Build
  ↓
DockerHub Push
  ↓
AWS EC2
  ↓
Running Flask API Container
