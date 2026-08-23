# Exercise 3: Scaling Flask App on Single Node using ReplicaSets

## Objective
Implement a real-life tech use-case: **E-commerce Flash Sale**.
Scale a Python Flask application across multiple pods using Kubernetes `ReplicaSet`, observe load distribution across pods, verify health and liveness probes, and test pod auto-healing.

## Architecture
- **Flask Application (`app.py`)**: Endpoints for homepage (`/`), flash sale purchase (`/buy`), and health probe (`/health`), showing pod hostname.
- **ReplicaSet (`flashsale-replicaset.yaml`)**:
  - Replicas: 3
  - Liveness probe: HTTP `/health` every 10s
  - Readiness probe: HTTP `/health` every 5s
  - Resource limits: 100m - 500m CPU, 128Mi - 256Mi Memory
- **Service**: ClusterIP service exposing the ReplicaSet on port 80 (target port 5000).

## Step-by-Step Instructions

### Step 1: Set Docker Environment to Minikube
```bash
eval $(minikube docker-env)
```

### Step 2: Build the Docker Image
```bash
docker build -t flashsale:1.0 .
```

### Step 3: Deploy the ReplicaSet and Service
```bash
kubectl apply -f flashsale-replicaset.yaml
```

### Step 4: Verify ReplicaSet and Pods
```bash
kubectl get replicasets
kubectl get pods -l app=flashsale -o wide
```

### Step 5: Test Load Balancing and Scaling
Port-forward or run a temporary pod to test traffic:
```bash
kubectl port-forward svc/flashsale-svc 8080:80 &
```
Send requests to observe different pods responding:
```bash
for i in {1..5}; do curl http://localhost:8080/buy; echo ""; done
```

### Step 6: Test Pod Self-Healing
Delete one pod manually:
```bash
kubectl delete pod $(kubectl get pods -l app=flashsale -o jsonpath='{.items[0].metadata.name}')
```
Verify ReplicaSet immediately spawns a new replacement pod to maintain the desired count of 3:
```bash
kubectl get pods -l app=flashsale
```

## Cleanup
```bash
kubectl delete -f flashsale-replicaset.yaml
```
