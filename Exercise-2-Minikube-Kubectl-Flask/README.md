# Exercise 2: Deploy a Flask App on Minikube using Kubectl and YAML

## Objective
The goal of this exercise is to build and containerize a simple Python Flask application and deploy it to a local single-node Kubernetes cluster using Minikube and declarative YAML manifests.

## Architecture
- **Flask Web Application**: Python microservice listening on port `15000`.
- **Docker Image**: Containerized as `flask-app:latest` using `python:3.9-slim`.
- **Kubernetes Deployment**: Manages the Flask pod replica.
- **Kubernetes Service**: `NodePort` exposing port `15000` to the host.

## Prerequisites
- Docker installed and running
- Minikube installed (`minikube version`)
- kubectl installed (`kubectl version --client`)

## Step-by-Step Instructions

### Step 1: Start Minikube
```bash
minikube start
```

### Step 2: Point Local Docker CLI to Minikube's Docker Daemon
To allow Minikube to access images built on your local system without pushing to Docker Hub:
```bash
eval $(minikube docker-env)
```

### Step 3: Build the Docker Image
```bash
docker build -t flask-app:latest .
```

Verify the image:
```bash
docker images | grep flask-app
```

### Step 4: Deploy Using Kubernetes Manifests
Apply the Deployment and Service:
```bash
kubectl apply -f flask-deployment.yaml
```

Verify deployment and pods:
```bash
kubectl get deployments
kubectl get pods -l app=flask-app
kubectl get svc flask-app-service
```

### Step 5: Access the Application
Get the accessible URL via Minikube tunnel/service:
```bash
minikube service flask-app-service
```
Or test using curl:
```bash
curl $(minikube service flask-app-service --url)
```

Expected Output:
```text
Hello from Flask on Kubernetes!
```

## Cleanup
```bash
kubectl delete -f flask-deployment.yaml
```
