# Sentimental-analysis
Ineuron internship project
This project aims to perform sentiment analysis on customer reviews using Apache Spark, S3, and HDFS. The sentiment analysis pipeline reads customer reviews from an S3 bucket, processes the data using Spark, and stores the results in HDFS. This readme provides an overview of the project, its features, and instructions for running the pipeline.

### Data-Set 
(https://drive.google.com/file/d/1ja_mGrJsLrkX5Stf20VrTi6R1uh36Eou/view?usp=sharing)

# Architecture:
![image](https://github.com/krishna7356/Sentimental-analysis/blob/main/Architecture-diagram-1.jpg)

# Features

* Data ingestion from S3: The pipeline reads customer reviews in CSV format from the specified S3 bucket location.
* Data processing using Spark: Apache Spark is utilized for reading data from s3 and write in to HDFS in parquet format customer review data.
* Storage in HDFS: The processed reviews and sentiment analysis results are stored in HDFS for persistent storage.
* Iterative execution and scheduling: The pipeline can be scheduled to run iteratively after each hour, ensuring continuous dumping data from s3 to HDFS

# Instructions

* Prerequisites:

  Apache Spark  and Hadoop  should be installed and configured.
  Ensure access to the specified S3 bucket and HDFS storage location.
  Set up necessary authentication credentials for accessing S3 and HDFS.

* Configuration:

  Update the configuration files (spark-config.json, s3-config.json, hdfs-config.json) with the appropriate credentials and file locations.
  Adjust any additional parameters in the configuration files according to your requirements.

* Execution:

  Run the main.py script to initiate the sentiment analysis pipeline.
  The pipeline will read the customer reviews from the specified S3 bucket and store the  data in to  HDFS.
