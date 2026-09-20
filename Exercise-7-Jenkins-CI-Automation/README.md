# Exercise 7: Introduction to Continuous Integration (CI) and Jenkins Automation

## What is Continuous Integration (CI)?
**Continuous Integration (CI)** is a fundamental DevOps software development practice where developers merge their code changes into a central repository frequently (multiple times a day). Each integration is automatically verified by automated builds and tests, allowing teams to detect defects early, reduce integration friction, and accelerate release cycles.

---

## Key Pillars of CI
1. **Frequent Integration**: Developers push small, incremental changes rather than massive late-stage merges.
2. **Automated Builds**: The CI server automatically triggers compilation, dependency resolution, and packaging upon every commit.
3. **Automated Testing**: Unit, functional, and regression test suites run automatically to validate changes.
4. **Immediate Feedback**: Developers receive notifications within minutes regarding build or test outcomes.

---

## Comparison of Leading CI/CD Tools

| Tool | Architecture | Key Characteristics | Ideal Use Case |
|---|---|---|---|
| **Jenkins** | Controller/Agent (Self-hosted) | Open-source, 1800+ plugins, extreme extensibility, declarative pipelines | Enterprise-grade customizable CI/CD |
| **GitHub Actions** | Hosted / Self-hosted Runners | Native GitHub integration, YAML workflows, marketplace actions | Projects hosted on GitHub |
| **GitLab CI/CD** | GitLab Runners | Fully integrated DevOps platform, Auto DevOps, YAML pipelines | Complete single-application DevOps lifecycle |
| **CircleCI** | Cloud / Server | Fast container execution, Docker layer caching, resource classes | Container-heavy microservices |
| **Travis CI** | Cloud | Pioneer in open-source CI, simple `.travis.yml` | Open-source multi-language libraries |
| **Azure DevOps** | Hosted / Self-hosted | Deep Microsoft & Azure integration, YAML/Classic UI pipelines | Microsoft ecosystem & enterprise clouds |
| **TeamCity** | Server / Build Agents | First-class Kotlin DSL, intelligent build history and test analytics | Complex polyglot enterprise architectures |
| **Bamboo** | Atlassian Stack | Direct Jira and Bitbucket synchronization | Teams committed to Atlassian suite |
| **Drone** | Container-native | Lightweight, every build step executes inside an ephemeral container | Cloud-native containerized pipelines |
| **Spinnaker** | Multi-Cloud CD | Advanced deployment strategies (Canary, Blue/Green), Kubernetes native | High-velocity cloud continuous delivery |

---

## Core Jenkins Concepts

```
+-------------------------------------------------------+
|                    JENKINS CONTROLLER                 |
|  - Web UI & REST API                                  |
|  - Plugin Manager                                     |
|  - Pipeline Orchestration Engine                      |
|  - Build Job Scheduler                                |
+---------------------------+---------------------------+
                            |
           +----------------+----------------+
           | Agent Protocol (Port 50000)     |
           v                                 v
+-----------------------+         +---------------------+
|   JENKINS AGENT 1     |         |   JENKINS AGENT 2   |
|  - Docker CLI         |         |  - Python / PyTest  |
|  - Build Workspace    |         |  - Build Workspace  |
+-----------------------+         +---------------------+
```

1. **Job / Project**: A runnable unit of automation (Freestyle, Pipeline, Multibranch).
2. **Build**: An individual execution of a job with a specific build number and log.
3. **Pipeline**: A suite of plugins supporting the modeling of simple-to-complex delivery pipelines via a `Jenkinsfile`.
4. **Plugins**: Extensions providing integration with Git, Docker, Kubernetes, Slack, JUnit, etc.
5. **Nodes & Agents**: Execution environments where builds run.

---

## Step-by-Step Jenkins Docker Setup

### Step 1: Launch Jenkins via Docker
Using Docker CLI:
```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```
*(Or use `docker compose up -d` with the provided `docker-compose.yml`)*

### Step 2: Retrieve the Initial Admin Password
Upon startup, Jenkins generates a secure initial password:
```bash
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
Copy the 32-character alphanumeric key.

### Step 3: Access Jenkins Web Interface
1. Open your browser and navigate to: `http://localhost:8080`
2. Paste the retrieved administrator password to unlock Jenkins.
3. Select **"Install suggested plugins"** to automatically install standard Git, Pipeline, and SCM plugins.
4. Create the First Admin User credentials.
5. Save and finish setup to reach the Jenkins Dashboard.
