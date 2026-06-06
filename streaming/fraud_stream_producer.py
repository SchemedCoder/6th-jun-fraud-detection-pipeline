from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# ====================================
# Spark Session
# ====================================

spark = (
    SparkSession.builder
    .appName("FraudDetectionStreaming")
    .config(
        "spark.sql.extensions",
        "io.delta.sql.DeltaSparkSessionExtension"
    )
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

# ====================================
# Transaction Schema
# ====================================

transaction_schema = StructType([
    StructField(
        "transaction_id",
        LongType(),
        True
    ),

    StructField(
        "customer_id",
        LongType(),
        True
    ),

    StructField(
        "amount",
        DoubleType(),
        True
    ),

    StructField(
        "country",
        StringType(),
        True
    ),

    StructField(
        "device_type",
        StringType(),
        True
    ),

    StructField(
        "event_time",
        StringType(),
