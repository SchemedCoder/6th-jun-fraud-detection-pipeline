# 6th-jun-fraud-detection-pipeline

# Real-Time Fraud Detection Platform

## Overview

This project simulates a banking fraud detection system using:

- Apache Kafka
- PySpark Structured Streaming
- Delta Lake
- SQL Analytics
- Python

The platform processes transaction events in real time and detects suspicious activity using fraud detection rules.

---

## Business Problem

Banks process millions of transactions daily.

Fraud analysts need immediate visibility into:

- High-value transactions
- Unusual customer activity
- Multiple transactions within seconds
- Transactions from suspicious countries
- New device usage

The objective is to identify fraudulent transactions as quickly as possible.

---

## Architecture

Transaction Generator
        ↓
Kafka Producer
        ↓
Kafka Topic
        ↓
PySpark Structured Streaming
        ↓
Bronze Layer
        ↓
Silver Layer
        ↓
Gold Layer
        ↓
Fraud Analytics

---

## Technology Stack

- Python
- Apache Kafka
- PySpark
- Delta Lake
- SQL
- Docker
- GitHub Actions
- Pytest

---

## Fraud Rules

### Rule 1

High Value Transaction

Flag:

amount > 50000

---

### Rule 2

Velocity Fraud

More than 3 transactions within 60 seconds.

---

### Rule 3

Country Risk

Transaction originates from risky country.

---

### Rule 4

New Device Detection

Customer uses unseen device.

---

### Rule 5

Impossible Travel

Transactions appear from geographically impossible locations within a short period.

---

## Medallion Architecture

Bronze

Raw transactions.

Silver

Validated and enriched transactions.

Gold

Fraud scores and business metrics.

---

## Running the Project

Start Kafka:

```bash
docker compose up -d
```

Generate transaction events:

```bash
python scripts/generate_transactions.py
```

Start Producer:

```bash
python streaming/kafka_producer.py
```

Start Streaming Consumer:

```bash
python streaming/fraud_stream_processor.py
```




