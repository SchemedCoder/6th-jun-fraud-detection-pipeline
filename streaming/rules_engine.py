from pyspark.sql.functions import *

# ------------------------------------
# Rule 1
# High Value Transaction
# ------------------------------------

def high_value_rule(df):

    return df.withColumn(
        "high_value_flag",

        when(
            col("amount") > 50000,
            1
        ).otherwise(0)
    )

# ------------------------------------
# Rule 2
# Risky Country
# ------------------------------------

def country_risk_rule(df):

    risky_countries = [
        "Nigeria",
        "Russia"
    ]

    return df.withColumn(
        "country_risk_flag",

        when(
            col("country")
            .isin(risky_countries),
            1
        ).otherwise(0)
    )

# ------------------------------------
# Rule 3
# New Device
# ------------------------------------

def device_risk_rule(df):

    return df.withColumn(
        "device_risk_flag",

        when(
            col("device_type")
            == "WEB",
            1
        ).otherwise(0)
    )

# ------------------------------------
# Rule 4
# Late Arriving Event
# ------------------------------------

def late_event_rule(df):

    return df.withColumn(
        "late_event_flag",

        when(
            col("late_event") == True,
            1
        ).otherwise(0)
    )

# ------------------------------------
# Final Fraud Score
# ------------------------------------

def calculate_fraud_score(df):

    return df.withColumn(

        "fraud_score",

        col("high_value_flag")
        +
        col("country_risk_flag")
        +
        col("device_risk_flag")
        +
        col("late_event_flag")
    )
