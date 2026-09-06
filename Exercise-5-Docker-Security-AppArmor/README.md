# Exercise 5: Docker Security with AppArmor and Python

## Objective
The goal of this exercise is to understand how to secure Docker containers using **AppArmor** profiles enforced via Linux security modules and automated using the **Docker SDK for Python**.

## Scenario
You are deploying a containerized Flask web application that requires confinement. To prevent potential container escape or unauthorized exploration:
- Access to sensitive system directories (e.g., `/etc`, `/var`) must be denied.
- Execution of binaries (e.g., `/bin/bash`, `cat`) must be restricted.
- Elevated Linux capabilities like `SYS_ADMIN` must be dropped.

---

## Prerequisites & Installation

On Linux / Ubuntu / Debian:
```bash
sudo apt-get update
sudo apt-get install -y apparmor-utils python3-pip
pip install docker
```

---

## Step-by-Step Instructions

### Step 1: Create the AppArmor Profile
Save the profile configuration in `/etc/apparmor.d/my-apparmor-profile` (or copy the local file):
```bash
sudo cp my-apparmor-profile /etc/apparmor.d/my-apparmor-profile
```

### Step 2: Load the Profile into the Linux Kernel
Load and parse the profile:
```bash
sudo apparmor_parser -r /etc/apparmor.d/my-apparmor-profile
```

Verify profile is active:
```bash
sudo aa-status | grep my-apparmor-profile
```

### Step 3: Build the Docker Image
```bash
docker build -t flask-apparmor .
```

### Step 4: Run Container with AppArmor Profile (CLI Method)
```bash
docker run -d --name flask-secure --security-opt="apparmor=my-apparmor-profile" -p 5000:5000 flask-apparmor
```

### Step 5: Automate Application via Docker SDK for Python
Run `apply_apparmor.py` to programmatically build the image, start the container with the security profile, and inspect its runtime parameters:
```bash
python3 apply_apparmor.py
```

Expected Output:
```text
Building Docker image: flask-apparmor...
Running container with AppArmor security-opt...
Container started: f8c2a7f9b9b8
Inspecting container to verify AppArmor profile...
AppArmor profile applied: ['apparmor=my-apparmor-profile']
Stopping and cleaning up container...
Finished successfully.
```

### Step 6: Test Restricted Actions
Run `test_restricted_actions.py` to verify that blocked actions are prevented:
```bash
python3 test_restricted_actions.py
```

Expected Output:
```text
Container started: f8c2a7f9b9b8
Attempt to read /etc/passwd: Exit Code 1, Output: 
Attempt to execute /bin/bash: Exit Code 126, Output: 
Container stopped and cleaned up.
```
*(Exit code 126 indicates "Permission denied" due to AppArmor denial).*

---

## Conceptual Questions & Answers

### 1. What is the purpose of using AppArmor with Docker containers?
AppArmor (Application Armor) is a Linux Security Module (LSM) that enforces Mandatory Access Control (MAC) policies. With Docker, it confines containers to a defined set of system resources, directories, capabilities, and system calls, adding defense-in-depth protection beyond container namespaces and cgroups.

### 2. How do AppArmor profiles help secure a Docker container?
AppArmor profiles specify allow and deny rules for file access, binary execution, network sockets, and capabilities. If an attacker gains code execution inside the container, AppArmor prevents them from tampering with the filesystem or running shell binaries.

### 3. Why is it important to restrict access to sensitive directories such as `/etc/` and `/var/`?
Directories like `/etc/` contain sensitive configuration files, user/group definitions (`/etc/passwd`, `/etc/shadow`), and TLS certificates. Restricting read/write access prevents credential theft, unauthorized reconnaissance, and system modification.

### 4. What other capabilities can you restrict using AppArmor profiles?
AppArmor can restrict:
- Network operations (e.g., raw sockets, binding privileged ports below 1024)
- Linux kernel capabilities (e.g., `sys_admin`, `sys_ptrace`, `net_admin`, `sys_chroot`)
- Execution of arbitrary binaries or shared libraries
- Mount/umount system calls

### 5. How can you verify if an AppArmor profile is successfully applied to a Docker container?
You can inspect the container using `docker inspect <container_id> --format '{{.HostConfig.SecurityOpt}}'` or through the Docker Python SDK (`container_info['HostConfig']['SecurityOpt']`). The output will explicitly list `apparmor=<profile_name>`.
