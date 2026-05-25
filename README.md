# IP Network Stream Monitor & Fault Detector

A real-time network monitoring and fault detection dashboard built using Python, FastAPI, Scapy, SQLite, WebSockets, and Chart.js.

This project captures live network traffic, analyzes TCP/UDP packets, stores traffic data in SQLite, detects abnormal traffic patterns, and visualizes network analytics through a live dashboard.

---

# Project Overview

The IP Network Stream Monitor & Fault Detector is designed to simulate a lightweight network observability and monitoring platform.

The system continuously captures live packets from the network interface, extracts important protocol-level information, stores metrics in a database, and streams analytics to a real-time dashboard.

The project demonstrates concepts related to:

- Network Packet Sniffing
- Traffic Monitoring
- Real-Time Data Streaming
- Protocol Analysis
- Fault/Anomaly Detection
- Backend API Development
- WebSocket Communication
- Dashboard Visualization

---

# Features

## Real-Time Packet Sniffing
- Captures live TCP and UDP packets using Scapy
- Extracts packet metadata from network streams
- Monitors incoming network traffic continuously

## Protocol Parsing
- Parses:
  - Source IP
  - Destination IP
  - Source Port
  - Destination Port
  - Packet Size
  - TCP Flags
  - Protocol Type

## SQLite Packet Logging
- Stores captured packet data into SQLite database
- Maintains persistent packet logs
- Enables analytics querying

## Real-Time Dashboard
- Live monitoring dashboard using HTML, CSS, JavaScript, and Chart.js
- Displays:
  - Total packets
  - TCP packets
  - UDP packets
  - Protocol distribution
  - Packet traffic trends

## Protocol Distribution Analytics
- Displays TCP vs UDP packet analytics
- Visualized using pie charts

## Traffic Visualization
- Real-time packet traffic graph
- Dynamic chart updates

## Top Active Source IP Analytics
- Detects most active traffic-generating IP addresses
- Uses SQL aggregation queries

## WebSocket-Based Live Alerts
- Streams anomaly alerts to dashboard in real time
- Event-driven architecture

## Threshold-Based Fault Detection
The system performs basic anomaly detection using:
- Packet burst detection
- Traffic spike monitoring
- Jitter spike monitoring
- Latency anomaly detection

---

# System Architecture

## High-Level Architecture

```text
                +----------------------+
                |   Network Traffic    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Scapy Packet       |
                |      Sniffer         |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |    Packet Parser     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Fault Detection     |
                |   & Analytics        |
                +----------+-----------+
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
+----------------------+       +----------------------+
| SQLite Database      |       | WebSocket Alerts     |
| Packet Logging       |       | Real-Time Streaming  |
+----------+-----------+       +----------+-----------+
           |                                 |
           +----------------+----------------+
                            |
                            v
                +----------------------+
                | FastAPI Backend API  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Live Dashboard UI    |
                | Chart.js Analytics   |
                +----------------------+
```

---

# Workflow Explanation

## Step 1 — Packet Capture
The system captures live network traffic using Scapy.

Scapy listens to raw packets flowing through the network interface and forwards them to the processing pipeline.

---

## Step 2 — Packet Parsing
Captured packets are parsed to extract useful networking information such as:
- IP addresses
- Ports
- Protocol types
- Packet sizes
- TCP flags

This converts raw packets into structured packet data.

---

## Step 3 — Packet Logging
Parsed packet information is stored in SQLite database for:
- persistent storage
- analytics
- monitoring queries

---

## Step 4 — Fault Detection
The detector module analyzes packet behavior to identify:
- abnormal packet bursts
- jitter spikes
- latency spikes
- suspicious traffic patterns

Threshold-based logic is used for anomaly detection.

---

## Step 5 — Real-Time API Layer
FastAPI provides backend APIs for:
- dashboard metrics
- traffic analytics
- top active IPs

---

## Step 6 — WebSocket Communication
WebSocket connections stream live alerts directly to the dashboard without requiring page refreshes.

---

## Step 7 — Dashboard Visualization
The frontend dashboard visualizes:
- packet metrics
- traffic trends
- protocol distribution
- active IP analytics
- live alerts

using Chart.js and dynamic JavaScript updates.

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Scapy | Packet Sniffing |
| FastAPI | Backend APIs |
| SQLite | Database Storage |
| WebSockets | Real-Time Communication |
| HTML/CSS/JavaScript | Frontend Dashboard |
| Chart.js | Data Visualization |

---

# Folder Structure

```text
network-stream-monitor/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── sniffer.py
│   ├── parser.py
│   ├── detector.py
│   ├── database.py
│   ├── websocket_manager.py
│
├── frontend/
│   └── index.html
│
├── screenshots/
│
├── requirements.txt
├── README.md
├── .gitignore
```

---

# Installation & Setup

## Step 1 — Clone Repository

```bash
git clone <your-github-repo-url>
cd network-stream-monitor
```

---

## Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 3 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

---

## Start Packet Sniffer

```bash
python -m app.sniffer
```

---

## Open Dashboard

Open:

```text
frontend/index.html
```

in browser.

---

# Dashboard Features

The dashboard displays:

- Total Packet Count
- TCP Packet Count
- UDP Packet Count
- Traffic Graph
- Protocol Distribution Pie Chart
- Top Active Source IPs
- Real-Time Alerts
- Jitter Metrics
- Latency Metrics

---

# Example Fault Detection Events

Examples of generated alerts:

```text
[ALERT] High packet burst detected
[ALERT] Jitter spike detected
[ALERT] High latency detected
```

---

# Future Improvements

- Advanced anomaly detection
- Machine learning-based traffic analysis
- Docker deployment
- Multi-device monitoring
- Real latency estimation
- Historical traffic analytics
- Authentication system
- RTP stream analysis

---

# Learning Outcomes

This project helped in understanding:

- Network packet analysis
- Real-time backend systems
- FastAPI APIs
- WebSocket communication
- Dashboard visualization
- Database integration
- Monitoring architectures
- Fault detection concepts

---

# Author

Sagar V Bidari

Artificial Intelligence & Machine Learning Engineering Student

Nitte Meenakshi Institute of Technology
