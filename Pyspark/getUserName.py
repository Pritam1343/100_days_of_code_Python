from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.appName("dropDuplicateRows").getOrCreate()
df=spark.read.format("csv").option("inferSchema","True").option("header","True").load("D:/customers-2000000.csv")
getUserName=df.withColumn("Domain Name",split(df["Email"],"@")[1])
# getUserName=getUserName.withColumnRenamed("split","UserName")
groupbydomain=getUserName.groupby("Domain Name").count()
groupbydomain=groupbydomain.withColumnRenamed("count","Domain Name count")
groupbydomain.show(100)