from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("FirstApp").getOrCreate()

rdd = spark.sparkContext.textFile("D:/data.csv")

rdd1=rdd.flatMap(lambda x:x.split(","))

rdd2=rdd1.map(lambda x:x.split("@")[1])

rdd3=rdd2.map(lambda x:(x,1))

rdd4=rdd3.reduceByKey(lambda x,y:x+y)

result=rdd4.collect()
print(result)
