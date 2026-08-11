# Flask Application Deployment on Amazon EKS

## Overview

This project demonstrates an end-to-end CI/CD pipeline for deploying a containerized Flask application to Amazon EKS using GitHub Actions.

### Tech Stack

- Python / Flask
- Pytest
- Docker
- GitHub Actions
- Amazon ECR
- Amazon EKS
- Kubernetes

## CI/CD Workflow

On every push to the `main` branch, GitHub Actions automatically:

1. Runs application tests using Pytest
2. Builds the Docker image
3. Pushes the image to Amazon ECR
4. Deploys the application to Amazon EKS
5. Verifies the Kubernetes deployment

## Architecture

Code → GitHub Actions → Pytest → Docker → Amazon ECR → Amazon EKS → LoadBalancer

## Kubernetes Deployment

The application runs on Amazon EKS with:

- 2 application replicas
- Kubernetes Deployment
- LoadBalancer Service
- Flask application running on port `5000`

## Security

GitHub Actions authenticates with AWS using OIDC and an IAM role, avoiding the use of long-lived AWS access keys.
