# Exercise 9: Jenkins Multi-Stage Pipeline: Deploying a Python Application

## Objective
Create and execute an automated **Jenkins Declarative Pipeline** spanning 5 distinct stages:
1. **Build**: Set up virtual environments and install dependencies (`requirements.txt`).
2. **Test**: Run automated unit test suite with Python's built-in `unittest` runner.
3. **Deploy**: Stage application binaries to a staging deployment directory.
4. **Run Application**: Launch the application daemon in the background with PID tracking.
5. **Test Application**: Execute integration tests against the active running application.
6. **Post-Actions Teardown**: Gracefully stop the application process.

---

## File Structure
- `app.py`: Flask web microservice returning `"Hello, Jenkins Multi-Stage Pipeline!"`.
- `requirements.txt`: Application dependencies (`flask==2.1.2`).
- `test_app.py`: Unit test verifying status code 200 and response payload.
- `Jenkinsfile`: Declarative Jenkins Pipeline orchestrating the multi-stage lifecycle.

---

## Step-by-Step Instructions

### Step 1: Run Local Tests
Verify tests pass locally:
```bash
python3 -m unittest discover -s .
```

Expected Output:
```text
[TEST OUTPUT] Response body: Hello, Jenkins Multi-Stage Pipeline!
.
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
```

---

### Step 2: Configure Jenkins Pipeline Job

1. Go to Jenkins Dashboard at `http://localhost:8080`.
2. Click **New Item** -> Name: `Python-MultiStage-Pipeline` -> Select **Pipeline** -> Click **OK**.
3. In the Configuration page under **Pipeline**:
   - **Definition**: `Pipeline script from SCM`
   - **SCM**: `Git`
   - **Repository URL**: `https://github.com/Arvindkumaravel/DevOps-Lab.git`
   - **Branches to build**: `*/main`
   - **Script Path**: `Exercise-9-Jenkins-Multi-Stage-Pipeline/Jenkinsfile`
4. Click **Save**.

---

### Step 3: Run the Pipeline & Inspect Stages

Click **Build Now**. Observe the Stage View in Jenkins UI:

```
[ Build ] ---> [ Test ] ---> [ Deploy ] ---> [ Run Application ] ---> [ Test Application ]
  (Green)       (Green)        (Green)             (Green)                  (Green)
```

Console Output Verification:
```text
Started by user Admin
Obtained Exercise-9-Jenkins-Multi-Stage-Pipeline/Jenkinsfile from git https://github.com/Arvindkumaravel/DevOps-Lab.git
[Pipeline] Start of Pipeline
[Pipeline] stage: Build
Stage 1: Installing dependencies and preparing build...
[Pipeline] stage: Test
Stage 2: Executing unit tests...
+ python3 -m unittest discover -s .
[TEST OUTPUT] Response body: Hello, Jenkins Multi-Stage Pipeline!
.
----------------------------------------------------------------------
Ran 1 test in 0.004s
OK
[Pipeline] stage: Deploy
Stage 3: Staging application files...
[Pipeline] stage: Run Application
Stage 4: Starting Flask application daemon...
[Pipeline] stage: Test Application
Stage 5: Validating running application endpoint...
.
OK
[Pipeline] stage: Post Actions
Teardown: Stopping background processes...
Pipeline completed successfully! All stages passed.
Finished: SUCCESS
```

---

## Troubleshooting Jenkins Environment Dependencies
If the Jenkins container lacks `python3`, `pip`, or `flask`, access the container as `root`:
```bash
docker exec -it -u root jenkins bash
apt-get update
apt-get install -y python3 python3-pip python3-flask python3-venv
exit
```
Then re-trigger the build in Jenkins.
