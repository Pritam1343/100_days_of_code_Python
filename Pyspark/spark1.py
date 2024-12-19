from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Sample").getOrCreate()

ls=[10,20,30,40,50]

rdd=spark.sparkContext.parallelize(ls)

rdd1=rdd.map(lambda x:x%2)


print(rdd1.collect())
