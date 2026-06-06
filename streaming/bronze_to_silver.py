from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = (
    SparkSession.builder
    .appName("BronzeToSilver")
    .getOrCreate()
)

bronze_df = spark.read.format(
    "delta"
).load(
    "delta/bronze_transactions"
)

silver_df = (
    bronze_df

    .dropDuplicates(
        ["transaction_id"]
    )

    .filter(
        col("amount") > 0
    )

    .withColumn(
        "late_event",
        when(
            (
                unix_timestamp(
                    "ingest_time"
                )
                -
                unix_timestamp(
                    "event_time"
                )
            ) > 300,
            True
        ).otherwise(False)
    )
)

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save(
        "delta/silver_transactions"
    )

print(
    "Silver Layer Created"
)
