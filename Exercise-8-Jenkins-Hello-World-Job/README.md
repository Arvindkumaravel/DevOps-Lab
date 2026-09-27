# Exercise 8: Creating "Hello World" Jenkins Job

## Objective
Create and execute your first automated build job in Jenkins by pulling a script from a Git repository and executing it via a Jenkins job.

---

## Files in this Exercise
- `hello-world.sh`: Executable Bash script outputting `"Hello, Jenkins!"`.
- `Jenkinsfile`: Declarative Pipeline script executing the script within a CI pipeline.

---

## Step-by-Step Instructions

### Step 1: Prepare the Script
Create `hello-world.sh` and make it executable:
```bash
chmod +x hello-world.sh
```

Test running locally:
```bash
./hello-world.sh
# Output: Hello, Jenkins!
```

---

### Step 2: Configure Jenkins Freestyle Job

1. Log into Jenkins at `http://localhost:8080`.
2. On the dashboard, click **New Item**.
3. Enter job name: `HelloWorld-Freestyle`.
4. Select **Freestyle project** and click **OK**.

#### General Settings
- **Description**: `First Hello World Jenkins job running shell script`.

#### Source Code Management (SCM)
- Select **Git**.
- **Repository URL**: `https://github.com/Arvindkumaravel/DevOps-Lab.git`
- **Branches to build**: `*/main`

#### Build Steps
- Click **Add build step** -> **Execute shell**.
- Enter command:
  ```bash
  sh Exercise-8-Jenkins-Hello-World-Job/hello-world.sh
  ```

#### Save & Execute
- Click **Save**.
- Click **Build Now** to trigger the build.

---

### Step 3: Verify Build Console Output

Navigate to **Build History** -> **#1** -> **Console Output**:
```text
Started by user Admin
Running as SYSTEM
Building in workspace /var/jenkins_home/workspace/HelloWorld-Freestyle
The recommended git tool is: NONE
using credential github-token
Cloning the remote Git repository
Cloning repository https://github.com/Arvindkumaravel/DevOps-Lab.git
 > git init /var/jenkins_home/workspace/HelloWorld-Freestyle # timeout=10
Fetching upstream changes from https://github.com/Arvindkumaravel/DevOps-Lab.git
 > git --version # 'git version 2.39.5'
Checking out Revision 826cf8f... (refs/remotes/origin/main)
 > git checkout -f 826cf8f... # timeout=10
Commit message: "Add Exercise 8: Jenkins Hello World Job and Git Integration"
[HelloWorld-Freestyle] $ /bin/sh -xe /tmp/jenkins89271638291.sh
+ sh Exercise-8-Jenkins-Hello-World-Job/hello-world.sh
Hello, Jenkins!
Finished: SUCCESS
```
