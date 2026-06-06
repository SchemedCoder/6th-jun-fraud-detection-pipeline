from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from rules_engine import *

spark = (
    SparkSession.builder
    .appName("SilverToGold")
    .getOrCreate()
)

df = spark.read.format(
    "delta"
).load(
    "delta/silver_transactions"
)

# ----------------------------
# Apply Fraud Rules
# ----------------------------

df = high_value_rule(df)

df = country_risk_rule(df)

df = device_risk_rule(df)

df = late_event_rule(df)

df = calculate_fraud_score(df)

# ----------------------------
# Fraud Category
# ----------------------------

df = df.withColumn(

    "fraud_category",

    when(
        col("fraud_score") >= 3,
        "HIGH"
    )

    .when(
        col("fraud_score") == 2,
        "MEDIUM"
    )

    .otherwise("LOW")
)

# ----------------------------
# Customer Risk
# ----------------------------

customer_risk = (

    df

    .groupBy(
        "customer_id"
    )

    .agg(

        avg(
            "fraud_score"
        ).alias(
            "avg_fraud_score"
        ),

        count("*").alias(
            "txn_count"
        )
    )
)

customer_risk.write \
    .format("delta") \
    .mode("overwrite") \
    .save(
        "delta/customer_risk"
    )

# ----------------------------
# Gold Transactions
# ----------------------------

df.write \
    .format("delta") \
    .mode("overwrite") \
    .save(
        "delta/gold_transactions"
    )

print(
    "Gold Layer Created"
)
