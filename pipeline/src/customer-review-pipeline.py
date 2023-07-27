import time
from conf.spark_config import create_spark_session

# read customer reviews from S3


def read_customer_reviews(spark):
    return spark.read.format("json") \
        .option("header", "true") \
        .load("s3://sentimental-analysis-project-ineuron/customer_reviews.json")

# write the reviews to HDFS


def write_reviews_to_hdfs(reviews):
    reviews.write.format("parquet") \
        .mode("append") \
        .save("hdfs://localhost:9000/user/krish/customer_reviews")


if __name__ == "__main__":
    # Create a Spark session
    spark = create_spark_session()

    # Schedule the pipeline to run iteratively after each hour
    while True:
        reviews = read_customer_reviews(spark)
        write_reviews_to_hdfs(reviews)
        time.sleep(3600)
