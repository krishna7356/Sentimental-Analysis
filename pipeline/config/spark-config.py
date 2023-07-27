from pyspark.sql import SparkSession


def create_spark_session():
    spark = SparkSession.builder \
        .appName("CustomerReviewPipeline") \
        .getOrCreate()
    return spark
