from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.appName("GroupByCity").getOrCreate()
df=spark.read.format("csv").option("header","True").option("inferSchema","True").load("D:/customers-2000000.csv")
# GroupByCity=df.groupby("City").count()
# GroupByCity=GroupByCity.withColumnRenamed("count","CustomerCount")
# GroupByCity.show()
filterdf=df.filter(df["Email"].isNull())
filterdf.show()