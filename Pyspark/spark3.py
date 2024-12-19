from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("emp_data").getOrCreate()


rdd=spark.sparkContext.textFile("D:/input.txt")

rdd_p=rdd.filter(lambda x:("Pune" in x))
rdd_m=rdd.filter(lambda x:("Mumbai" in x))
rdd_d=rdd.filter(lambda x:("Delhi" in x))

print(rdd_p.count())
print(rdd_m.count())
print(rdd_d.count())
