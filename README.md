# 🚀 Python Task API with CI/CD (Jenkins + Docker + Kubernetes)

## 📌 Project Overview

This project is a FastAPI-based Task Management API with full CI/CD automation using Jenkins, Docker, and Kubernetes (Minikube). The project demonstrates best practices in backend development, containerization, containers orchestration and CI/CD automation.

### Features
- FastAPI backend with CRUD operations for tasks
- Modular structure (`main.py`, `routes.py`, `models.py`)
- Dockerized application
- Automated CI/CD pipeline using **Jenkins**
- Deployment on **Kubernetes (Minikube)**
- Automatic image build & push to Docker Hub on code changes

---

## 🛠 Tech Stack

- **Backend**: Python + FastAPI
- **Containerization**: Docker
- **CI/CD**: Jenkins
- **Orchestration**: Kubernetes (Minikube)
- **Version Control**: Git + GitHub

---

## 🏗 Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/KanchanaKoralage1/python-task-app.git
cd python-task-app/backend
```
### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Application
```bash
uvicorn app.main:app --reload
```

### 5.Open your browser:

- **App**  http://127.0.0.1:8000/
- **Swagger Docs**  http://127.0.0.1:8000/docs

---

## 🐳 Docker
### Build & Run Docker Image
```bash
docker build -t taskapi:v1 .
```

### Push to Docker Hub
```bash
docker tag taskapi:v1 yourusername/taskapi:v1
docker push yourusername/taskapi:v1
```

---

## 🔄 CI/CD Pipeline (Jenkins)

- A complete CI/CD pipeline is implemented using Jenkins with the following flow:
**Git Push → Jenkins → Docker Build → Push to Docker Hub → Kubernetes Deployment**

## Jenkins Setup

### 1.Run Jenkins using Docker:
```bash
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```
### 2.Access Jenkins at http://localhost:8080

### 3.Get initial admin password:
```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
### 4.Configure Docker Hub credentials in Jenkins
### 5.Create a Pipeline job pointing to this repository with Jenkinsfile

### 6.The pipeline automatically:

- Triggers on every push to main branch (via Poll SCM)
- Builds the Docker image
- Pushes it to Docker Hub
- Updates the Kubernetes deployment on Minikube

---

## ☸️ Kubernetes Deployment (Minikube)

### 1.Start Minikube
```bash
minikube start
```
### 2.Deploy
```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```
### 3.Access the Application
```bash
minikube service task-api-service -n taskapi
```
### 4.Check pods & services:
```bash
kubectl get all -n taskapi
```
---

## 📋 Next Steps / Future Improvements

- Add PostgreSQL database with SQLAlchemy + Alembic
- Implement proper Task models with Pydantic v2
- Add authentication (JWT)
- Write unit & integration tests
- Add monitoring (Prometheus + Grafana)
- Deploy to cloud (EKS / GKE / AKS)

---

## What I Have Implemented

- ✅ FastAPI CRUD Task Application
- ✅ Proper project structure with routers & models
- ✅ Dockerization
- ✅ Full CI/CD pipeline with Jenkins
- ✅ Automated Docker build & push to Docker Hub
- ✅ Kubernetes manifests & deployment on Minikube
- ✅ Git branching strategy (main + development)

