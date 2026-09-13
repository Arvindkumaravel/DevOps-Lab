# Exercise 6: Real-Time Operations Monitoring and Alerting (Quick-Commerce Platform)

## Objective
As a DevOps engineer managing a fast-paced delivery service ("ZAPPTTO"), you will implement an end-to-end operational monitoring, visualization, and alerting stack using:
- **Python Prometheus Client**: To simulate delivery traffic and expose runtime metrics.
- **Prometheus**: To scrape time-series metrics and evaluate alert conditions.
- **Grafana**: To visualize operational metrics via dashboards.
- **Jenkins**: To automate the deployment pipeline via a declarative `Jenkinsfile`.

---

## Architecture & Metric Flow

```
[delivery_metrics.py] 
       | (exposes /metrics on port 8000)
       v
  [Prometheus]  <--- scrapes every 15s
   (Port 9090)  <--- evaluates alert_rules.yml (HighPendingDeliveries, HighAverageDeliveryTime)
       |
       v
   [Grafana]    <--- queries Prometheus datasource
  (Port 3000)   <--- displays operational dashboards
```

---

## Metric Definitions

1. `total_deliveries` (`Gauge`): Total deliveries in system (pending + on_the_way + delivered).
2. `pending_deliveries` (`Gauge`): Number of pending deliveries awaiting rider assignment.
3. `on_the_way_deliveries` (`Gauge`): Deliveries currently in transit.
4. `average_delivery_time` (`Summary`): Distribution and observe values for order fulfillment latency.

---

## Step-by-Step Instructions

### Step 1: Run via Docker Compose (Recommended)
```bash
docker compose up -d
```

### Step 2: Verify Metrics Endpoint
```bash
curl http://localhost:8000/metrics
```

### Step 3: Access Prometheus UI
1. Navigate to: `http://localhost:9090`
2. Go to **Status** -> **Targets** to confirm `delivery_service` is `UP`.
3. Go to **Alerts** to monitor active alert rules:
   - `HighPendingDeliveries`: `pending_deliveries > 10`
   - `HighAverageDeliveryTime`: `(average_delivery_time_sum / average_delivery_time_count) > 30`

### Step 4: Access Grafana & Build Dashboard
1. Navigate to: `http://localhost:3000`
2. Log in with `admin` / `admin`.
3. Add Prometheus as a Data Source:
   - URL: `http://prometheus:9090` (or `http://localhost:9090`)
   - Click **Save & Test**.
4. Create a Dashboard with 4 Panels:
   - **Panel 1**: `total_deliveries` (Stat or Time Series)
   - **Panel 2**: `pending_deliveries` (Threshold alert highlighting at > 10)
   - **Panel 3**: `on_the_way_deliveries` (Gauge)
   - **Panel 4**: `average_delivery_time_sum / average_delivery_time_count` (Graph)

### Step 5: Jenkins Pipeline Automation
Create a Pipeline job in Jenkins pointing to the repository's `Jenkinsfile`:
- **Stage 1**: Pre-check Docker daemon availability.
- **Stage 2**: Build container image for the delivery metrics application.
- **Stage 3**: Run the delivery metrics container.
- **Stage 4**: Deploy Prometheus and Grafana containers with alert rules.

---

## Simulating Critical Alerts
To trigger alerts deliberately:
Modify `simulate_delivery()` in `delivery_metrics.py`:
```python
pending = random.randint(50, 100)  # Exceeds threshold of 10
```
Restart the metrics service:
```bash
docker compose restart delivery-metrics
```
Check Prometheus UI (`http://localhost:9090/alerts`) to observe `HighPendingDeliveries` transitioning from **PENDING** to **FIRING**.
