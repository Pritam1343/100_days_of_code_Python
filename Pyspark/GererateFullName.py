from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, upper
from pyspark.sql.types import StringType

spark=SparkSession.builder.appName("generateFullName").getOrCreate()

df=spark.read.format("csv").option("Header","True").option("Inferschema","True").load("D:/customers-2000000.csv")

df.createOrReplaceTempView("FullName")

query="""
select `Customer Id`,concat(`First Name`,' ',`Last Name`) as `Full Name` from FullName
"""

df1=spark.sql(query)

df1=df1.withColumn("Full Name",upper(df1["Full Name"]))

df1.show()
