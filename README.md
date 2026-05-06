# Calculator API CI/CD Pipeline

A minimal Python Flask calculator API deployed using a complete DevOps CI/CD pipeline.

This project demonstrates automated testing, code quality scanning, Docker image publishing, and automatic deployment to AWS EC2.

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
Pytest Tests
  ↓
SonarCloud Scan
  ↓
Docker Image Build
  ↓
DockerHub Push
  ↓
SSH Deploy to AWS EC2
  ↓
Running Flask API Container

