import phonenumbers
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Define a UDF to normalize phone numbers
def normalize_phone_number(phone, default_country="US"):
    try:
        # Parse and format the phone number
        parsed_number = phonenumbers.parse(phone, default_country)
        if phonenumbers.is_valid_number(parsed_number):
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        else:
            return None  # Return None for invalid numbers
    except Exception:
        return None  # Handle parsing errors

# Register the UDF
normalize_phone_udf = udf(normalize_phone_number, StringType())

spark=SparkSession.builder.appName("Normalize_phone_number").getOrCreate()
df=spark.read.format("csv").option("header","True").option("inferSchema","True").load("D:/customers-2000000.csv")

normalize_phone=df.withColumn("Normalized phone number",normalize_phone_udf(df["Phone 1"]))

normalize_phone.createOrReplaceTempView("normalize_phone_no")

query = """
select `Customer Id`, 
       concat(`First Name`, ' ', `Last Name`) as `Full Name`, 
       `Phone 1`,`Normalized phone number`
from normalize_phone_no 
where `Normalized phone number` IS NOT NULL
"""

df1 = spark.sql(query)
df1.show()
