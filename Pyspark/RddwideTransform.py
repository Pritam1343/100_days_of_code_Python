from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("Wide Transformation").getOrCreate()

# Read the text file
rdd = spark.sparkContext.textFile("D:/sample_emails_100.csv")

# Transformations
rdd1 = rdd.flatMap(lambda x: x.split(","))
rdd2 = rdd1.filter(lambda x: "@" in x).map(lambda x: x.split("@")[0])
# rdd3 = rdd2.map(lambda x: (x, 1))
# rdd4 = rdd3.reduceByKey(lambda x, y: x + y)

# Action to collect and print the results
result = rdd2.collect()
print(result)
print(rdd2.getNumPartitions())
