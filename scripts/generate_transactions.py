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

print("Generating transactions...")

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
        start_date="-30
