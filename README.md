# DevOps Lab Exercises (AY2025-2026)

Comprehensive laboratory exercises covering **Kubernetes**, **Docker Networking**, **Container Security (AppArmor)**, **Real-Time Monitoring (Prometheus & Grafana)**, and **Continuous Integration (Jenkins Pipelines)**.

---

## Repository Structure & Exercise Index

| Exercise | Module | Description | Technologies |
|---|---|---|---|
| [**Exercise 1**](./Exercise-1-Hello-Pod/) | **Kubernetes Basics** | Getting started with Kubernetes Pods and Services (Declarative & Imperative). | `Minikube`, `kubectl`, `Nginx` |
| [**Exercise 2**](./Exercise-2-Minikube-Kubectl-Flask/) | **K8s Deployments** | Deploying a containerized Flask microservice on Minikube with Deployments & Services. | `Minikube`, `Flask`, `Docker` |
| [**Exercise 3**](./Exercise-3-Minikube-Scaling-Flask-App-with-Replicasets/) | **K8s Scaling & Probes** | Scaling Flask apps using ReplicaSets with liveness/readiness probes (Flash Sale scenario). | `Kubernetes`, `ReplicaSet`, `Probes` |
| [**Exercise 4**](./Exercise-4-Docker-Networking/) | **Docker Networking** | Multi-container architecture on a custom bridge network with Flask, MySQL, and Redis. | `Docker`, `Bridge Network`, `DNS` |
| [**Exercise 5**](./Exercise-5-Docker-Security-AppArmor/) | **Container Security** | Securing Docker containers with AppArmor profiles and Python Docker SDK enforcement. | `AppArmor`, `Docker SDK`, `Security` |
| [**Exercise 6**](./Exercise-6-Grafana-Realtime-Monitoring-of-Quick-Commerce-App/) | **Monitoring & Alerts** | Real-time operations monitoring and automated alerting with Prometheus & Grafana. | `Prometheus`, `Grafana`, `Python Client` |
| [**Exercise 7**](./Exercise-7-Jenkins-CI-Automation/) | **CI/CD Foundations** | Jenkins installation, architecture, and comprehensive CI tool comparisons. | `Jenkins`, `Docker`, `CI/CD` |
| [**Exercise 8**](./Exercise-8-Jenkins-Hello-World-Job/) | **Jenkins Freestyle** | Building and executing a "Hello World" Jenkins build job from a Git repository. | `Jenkins`, `Bash`, `Git SCM` |
| [**Exercise 9**](./Exercise-9-Jenkins-Multi-Stage-Pipeline/) | **Jenkins Pipelines** | Declarative multi-stage pipeline: Build, Unit Test, Deploy, Daemon Execution, Validation. | `Jenkins Pipeline`, `unittest`, `Flask` |
| [**Exercise 10**](./Exercise-10-Minikube-Multi-Node-Multi-App-Minikube-Deployment/) | **Multi-Node K8s** | High-availability multi-node Minikube cluster with Pod Anti-Affinity rules and ReplicaSets. | `Multi-Node K8s`, `PodAntiAffinity` |

---

## Prerequisites & Tooling
Ensure the following tools are installed in your environment:
- **Docker**: Container runtime and image builder (`docker --version`)
- **Minikube**: Local Kubernetes cluster orchestrator (`minikube version`)
- **kubectl**: Kubernetes command line client (`kubectl version --client`)
- **Python 3.8+**: Application development runtime (`python3 --version`)
- **Jenkins**: CI automation server (runnable via Docker)

---

## Author
- **Arvind Kumaravel** ([@Arvindkumaravel](https://github.com/Arvindkumaravel))
