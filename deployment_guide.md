# 🚀 LiveApp Cloud Deployment Guide

> **Tournament**: OpenCV AI Competition 2026 (powered by AWS)  
> **Application**: PHANToM Grid :: Autonomous Agentic Vision Nexus  
> **Port**: 8088 (HTTP) | MCP Stdio/SSE: 8089  

---

## 1. Local Run
```bash
python live_app.py
```
Open your browser at `http://127.0.0.1:8088/` or probe `http://127.0.0.1:8088/healthz`.

---

## 2. Docker Deployment
```bash
docker build -t phantom-grid-opencv-nexus:latest .
docker run -d -p 8088:8088 phantom-grid-opencv-nexus:latest
```

---

## 3. Endpoints
- `/healthz`: ASIL-D health check returning JSON telemetry and ZDR zero-remanence confirmation.
- `/api/telemetry`: Microsecond OpenCV 5 feature extraction throughput and Bedrock actuation telemetry.
- `/`: Interactive dark-cyber visual telemetry status dashboard.
