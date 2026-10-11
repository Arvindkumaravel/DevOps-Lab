# Exercise 10: Multi-Node Kubernetes Cluster with Multiple Applications and ReplicaSets

## Storyboard & Architecture
Consider an e-commerce platform with two core microservices:
1. **Product Catalog** (`product-catalog`): Exposes available merchandise.
2. **Shopping Cart** (`shopping-cart`): Handles cart additions and inquiries.

To ensure high availability and fault tolerance:
- **Product Catalog** is deployed with 2 replicas across distinct nodes.
- **Shopping Cart** is deployed with 3 replicas across distinct nodes.
- Kubernetes **`podAntiAffinity`** rules with topology key `kubernetes.io/hostname` ensure that no two replicas of the same service run on the same physical or virtual worker node.

---

## Files in this Directory
- `product_catalog.py`: Flask microservice returning product catalog data.
- `shopping_cart.py`: Flask microservice for cart manipulation (GET / POST).
- `Dockerfile.product`: Container build manifest for Product Catalog.
- `Dockerfile.shopping`: Container build manifest for Shopping Cart.
- `product_catalog_deployment.yaml`: Deployment with 2 replicas + `podAntiAffinity`.
- `shopping_cart_deployment.yaml`: Deployment with 3 replicas + `podAntiAffinity`.
- `product_catalog_service.yaml`: NodePort Service for Product Catalog.
- `shopping_cart_service.yaml`: NodePort Service for Shopping Cart.

---

## Step-by-Step Instructions

### Step 1: Start Minikube with 3 Nodes
Clean up previous Minikube profile and initialize a 3-node cluster:
```bash
minikube stop
minikube delete
minikube start --nodes 3 -p devops-multinode
```

Verify cluster nodes:
```bash
kubectl get nodes
```
Expected output:
```text
NAME                     STATUS   ROLES           AGE   VERSION
devops-multinode         Ready    control-plane   1m    v1.31.0
devops-multinode-m02     Ready    <none>          45s   v1.31.0
devops-multinode-m03     Ready    <none>          30s   v1.31.0
```

---

### Step 2: Build Images and Load into Minikube Nodes
Build both microservice images:
```bash
docker build -t product-catalog:latest -f Dockerfile.product .
docker build -t shopping-cart:latest -f Dockerfile.shopping .
```

Load the images directly into all Minikube cluster nodes:
```bash
minikube -p devops-multinode image load product-catalog:latest
minikube -p devops-multinode image load shopping-cart:latest
```

---

### Step 3: Deploy Applications and Services
Apply deployments and service manifests:
```bash
kubectl apply -f product_catalog_deployment.yaml
kubectl apply -f shopping_cart_deployment.yaml
kubectl apply -f product_catalog_service.yaml
kubectl apply -f shopping_cart_service.yaml
```

---

### Step 4: Verify Pod Anti-Affinity and Node Distribution
Inspect the running pods and observe the `NODE` column:
```bash
kubectl get pods -o wide
```

Expected Output:
```text
NAME                               READY   STATUS    RESTARTS   AGE   IP           NODE                   NOMINATED NODE   READINESS GATES
product-catalog-5fdfc7f5fb-2jlnv   1/1     Running   0          29s   10.244.1.3   devops-multinode-m02   <none>           <none>
product-catalog-5fdfc7f5fb-7v556   1/1     Running   0          29s   10.244.2.4   devops-multinode-m03   <none>           <none>
shopping-cart-788c48675b-7l4lx     1/1     Running   0          25s   10.244.0.4   devops-multinode       <none>           <none>
shopping-cart-788c48675b-d48w2     1/1     Running   0          25s   10.244.1.4   devops-multinode-m02   <none>           <none>
shopping-cart-788c48675b-hml9r     1/1     Running   0          25s   10.244.2.5   devops-multinode-m03   <none>           <none>
```
*Notice how replicas are evenly distributed across `devops-multinode`, `devops-multinode-m02`, and `devops-multinode-m03`.*

---

### Step 5: Test Endpoints via Minikube Service Tunnel

#### Expose Services:
```bash
minikube -p devops-multinode service product-catalog-service --url
minikube -p devops-multinode service shopping-cart-service --url
```

#### Test Product Catalog:
```bash
curl http://<service-url>/products
```
Response:
```json
[
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800},
    {"id": 3, "name": "Headphones", "price": 150}
]
```

#### Test Shopping Cart:
```bash
# View empty cart
curl http://<service-url>/cart

# Add item to cart
curl -X POST http://<service-url>/cart \
     -H "Content-Type: application/json" \
     -d '{"id": 1, "name": "Laptop", "quantity": 1}'
```
Response:
```json
[
    {"id": 1, "name": "Laptop", "quantity": 1}
]
```

---

## Cleanup
```bash
kubectl delete -f product_catalog_service.yaml
kubectl delete -f shopping_cart_service.yaml
kubectl delete -f product_catalog_deployment.yaml
kubectl delete -f shopping_cart_deployment.yaml
minikube stop -p devops-multinode
```
