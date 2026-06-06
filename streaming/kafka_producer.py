import json
import time
import pandas as pd

from kafka import KafkaProducer

# ----------------------------------
# Kafka Configuration
# ----------------------------------

KAFKA_BROKER = "localhost:9092"

TOPIC_NAME = "bank_transactions"

# ----------------------------------
# Create Producer
# ----------------------------------

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

print("Connected to Kafka")

# ----------------------------------
# Load Dataset
# ----------------------------------

df = pd.read_csv(
    "data/sample/transactions.csv"
)

print(
    f"Loaded {len(df)} transactions"
)

# ----------------------------------
# Stream Records
# ----------------------------------

for _, row in df.iterrows():

    event = {
        "transaction_id": int(
            row["transaction_id"]
        ),

        "customer_id": int(
            row["customer_id"]
        ),

        "amount": float(
            row["amount"]
        ),

        "country": str(
            row["country"]
        ),

        "device_type": str(
            row["device_type"]
        ),

        "event_time": str(
            row["event_time"]
        ),

        "ingest_time": str(
            row["ingest_time"]
