

from pyspark.sql.functions import upper, lower, lit

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DataType, StringType, FloatType, BooleanType, \
    TimestampType
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("CSV processing").getOrCreate()

# read
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("D:/customers-2000000.csv")

# df.show()

df.createOrReplaceTempView("cust")
# query1="select * from cust"
query = """
select City ,count(`Customer Id`) as Customer_count from cust group by City
"""


df1 = spark.sql(query)
# df2=spark.sql(query1)
# df2.show(100)
# df1.printSchema()
# df1.show(20000)

# df1.write.format("JSON").save("D:/cust_op")
# schema=StructType([
#     StructField("First Name",StructType(),True),
#     StructField("Last Name",StringType(),True),
#     StructField("City",StringType(),True),
#     StructField("Year_of_subscription",DataType(),True),
#     StructField("rn",IntegerType(),True)
# ])


# df.show(100)

schema = StructType([
    StructField("Index", IntegerType(), True),
    StructField("Customer Id", StringType(), True),
    StructField("First Name", StringType(), True),
    StructField("Last Name", StringType(), True),
    StructField("Company", StringType(), True),
    StructField("City", StringType(), True),
    StructField("Country", StringType(), True),
    StructField("Phone 1", StringType(), True),
    StructField("Phone 2", StringType(), True),
    StructField("Email", StringType(), True),
    StructField("Subscription Date", TimestampType(), True),
    StructField("Website", StringType(), True)
])

# df1 = df.withColumn("First Name", lower(df["First Name"]))
# df2 = df.withColumn("Country", when(df['Country'] == "Marshall Islands", lit("M I")).otherwise(df['Country']))
# # df3 = df2.filter(df2["Country"] == "M I")
#
# df3=df.filter(df['Customer Id'].isNotNull() | df['Email'].isNotNull() | df["Subscription Date"].isNotNull())


# def isCountryEquals(country):
#     if country == "M I":
#         return country
#     else:
#         None
#
# isCountryEquals=udf(isCountryEquals,StringType())
# df3=df2.withColumn("Country",isCountryEquals(df2['Country']))
df1.show(1000)