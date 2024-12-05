from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('Spark').getOrCreate()
rdd=spark.sparkContext.parallelize([10,20,30,40,100])
rdd.collect()