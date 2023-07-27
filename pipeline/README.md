# Sentimental analysis

This project is a PySpark pipeline for processing customer reviews from an S3 bucket and storing the results in HDFS. The pipeline is designed to be run on a local machine with Spark in standalone mode.

## Prerequisites

Before running the pipeline, you need to install the following dependencies:

1. [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/javase-downloads.html): Required for running Spark.
2. [Apache Spark](https://spark.apache.org/downloads.html): The distributed computing framework used for data processing.
3. [Hadoop](https://hadoop.apache.org/releases.html): Required by Spark for distributed storage (HDFS).
4. [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/): For accessing files from S3.

## Installation

### 1. Install Java Development Kit (JDK)

Please download and install the latest version of JDK from the official Oracle website.

### 2. Install Apache Spark

1. Download the latest pre-built version of Spark from the Apache Spark website.
2. Extract the downloaded archive to a directory of your choice.
3. Set the `SPARK_HOME` environment variable to the Spark installation directory.

### 3. Install Hadoop

1. Download the latest Hadoop distribution from the Apache Hadoop website.
2. Extract the downloaded archive to a directory of your choice.
3. Set the `HADOOP_HOME` environment variable to the Hadoop installation directory.

### 4. Configure AWS CLI

1. Install the AWS CLI using the package manager of your choice (pip, apt, yum, etc.).
2. Configure the AWS CLI with your access key and secret key using the `aws configure` command.

## Running the Pipeline

1. Start HDFS:

```
$HADOOP_HOME/sbin/start-dfs.sh
```

2. Run the PySpark pipeline:

```
$SPARK_HOME/bin/spark-submit --master local[2] src/customer_review_pipeline.py
```

## Configuration

### AWS Access

The pipeline assumes you have set up the AWS CLI with proper credentials to access the S3 bucket where the `customer_reviews.json` file is located.

### Spark Configuration

The Spark session configuration, including the application name, can be adjusted in the `conf/spark_config.py` file.

## Output

The processed customer reviews will be written to HDFS at the following location:

```
hdfs://localhost:9000/user/krish/customer_reviews
```

## Additional Notes

- For larger-scale data processing, consider setting up a full-fledged Hadoop cluster and configuring Spark to run in a distributed mode.

- Please ensure that you have the necessary permissions to read from the S3 bucket and write to HDFS.

- For advanced PySpark configurations, please refer to the official [PySpark documentation](https://spark.apache.org/docs/latest/api/python/index.html).

---

I have tailored this README file to provide comprehensive instructions for setting up and running the Customer Review Pipeline using PySpark. I have also included notes on best practices and considerations for scalability. If you encounter any issues or have further questions, don't hesitate to reach out. Happy data processing!
