from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark=SparkSession.builder.appName("dropDuplicateRows").getOrCreate()

df=spark.read.format("csv").option("inferSchema","True").option("header","True").load("D:/customers-2000000.csv")
# df.printSchema()
dropDuplicate=df.drop_duplicates(["Customer Id","Email"])
dropDuplicate.show()

