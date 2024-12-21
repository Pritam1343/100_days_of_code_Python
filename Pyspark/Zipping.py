from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Zipping").getOrCreate()

rdd=spark.sparkContext.parallelize([1,3,5,7])
rdd1=rdd.map(lambda x: x*x)
rdd2=rdd.zip(rdd1)
print(rdd2.collect())

# Output : [(1, 1), (3, 9), (5, 25), (7, 49)]