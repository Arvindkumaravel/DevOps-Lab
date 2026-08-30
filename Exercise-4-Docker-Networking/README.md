# Exercise 4: Docker Networking with Multiple Containers

## Objective
Understand Docker networking concepts and configure a multi-container application communicating over a custom user-defined bridge network.

## Scenario
Develop and deploy a multi-container web application composed of:
1. **Python Flask Web Server** (Container 1)
2. **MySQL Database** (Container 2)
3. **Redis Cache** (Container 3)

All containers reside on an isolated bridge network, allowing secure inter-container communication using automatic DNS name resolution.

---

## Tasks & Step-by-Step Walkthrough

### Task 1: Create a Custom Bridge Network
Create a user-defined bridge network named `my-bridge-net`:
```bash
docker network create --driver bridge my-bridge-net
```

### Task 2: Verify the Network
List active Docker networks to confirm creation:
```bash
docker network ls
```

### Task 3: Inspect the Network
Inspect the configuration, subnet, gateway, and attached containers:
```bash
docker network inspect my-bridge-net
```

### Task 4: Build and Launch Containers
1. Build the Flask image:
```bash
docker build -t flask-api .
```

2. Run the MySQL, Redis, and Flask containers on `my-bridge-net`:
```bash
# Launch MySQL container
docker run -d --name mysql --net=my-bridge-net -e MYSQL_ROOT_PASSWORD=rootpassword mysql:latest

# Launch Redis container
docker run -d --name redis --net=my-bridge-net redis:latest

# Launch Flask container
docker run -d --name flask --net=my-bridge-net -p 5001:5001 flask-api
```

*(Alternatively, run all services using `docker compose up -d`)*

### Task 5: Test Connectivity & DNS Resolution
Enter the running Flask container shell:
```bash
docker exec -it flask bash
```

Test network reachability using container hostnames (Docker internal DNS):
```bash
# Ping MySQL by container name
ping -c 3 mysql

# Ping Redis by container name
ping -c 3 redis

# Exit container
exit
```

Test the REST API endpoint from the host:
```bash
curl http://localhost:5001/about
```

Expected Response:
```json
{
  "description": "This is a simple REST API built with Flask.",
  "name": "Simple REST API",
  "version": "1.0"
}
```

### Task 6: Cleanup
Stop and remove containers and network:
```bash
docker stop mysql redis flask && docker rm mysql redis flask
docker network rm my-bridge-net
```

---

## Conceptual Questions & Answers

### 1. What is the purpose of the `--net` flag in `docker run`?
The `--net` (or `--network`) flag specifies the Docker network that the container should connect to at launch. This allows the container to communicate with other containers on the same network using isolated routing and container name resolution.

### 2. How do containers communicate with each other on the same network?
Containers connected to a user-defined bridge network communicate using an embedded DNS server in Docker. When a container references another container by its name (e.g., `mysql` or `redis`), Docker's DNS automatically resolves the name to the target container's private IP address on that network.

### 3. What is the difference between a bridge network and a host network?
- **Bridge Network**: Provides private network virtualization and isolation. Containers get their own IP addresses on an internal subnet and talk to each other via internal routing. Ports must be explicitly mapped (`-p`) to be accessible from the host.
- **Host Network**: Removes network isolation between the container and the Docker host. The container shares the host's networking namespace directly (no separate IP or port forwarding).

### 4. How can you expose a container's port to the host machine?
Use the `-p` or `--publish` flag with the syntax `-p <HOST_PORT>:<CONTAINER_PORT>` (e.g., `-p 5001:5001`). This forwards incoming traffic on host port 5001 to container port 5001.
