from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import os

fake = Faker()

os.makedirs("data/sample", exist_ok=True)

NUM_CUSTOMERS = 5000
NUM_TRANSACTIONS = 100000

COUNTRIES = [
    "India",
    "USA",
    "Germany",
    "Singapore",
    "UK",
    "Australia",
    "Brazil",
    "Nigeria",
    "Russia",
    "China"
]

DEVICES = [
    "ANDROID",
    "IPHONE",
    "WEB",
    "TABLET"
]

transactions = []

for txn_id in range(1, NUM_TRANSACTIONS + 1):

    customer_id = random.randint(
        1,
        NUM_CUSTOMERS
    )

    amount = round(
        random.uniform(10, 10000),
        2
    )

    country = random.choice(
        COUNTRIES
    )

    device = random.choice(
        DEVICES
    )

    event_time = fake.date_time_between(
        start_date="-30d",
        end_date="now"
    )

    ingest_time = (
        event_time +
        timedelta(
            seconds=random.randint(
                0,
                300
            )
        )
    )

    transactions.append(
        {
            "transaction_id": txn_id,
            "customer_id": customer_id,
            "amount": amount,
            "country": country,
            "device_type": device,
            "event_time": event_time,
            "ingest_time": ingest_time
        }
    )

df = pd.DataFrame(transactions)

df.to_csv(
    "data/sample/transactions.csv",
    index=False
)

print(
    f"{len(df)} transactions generated"
)
